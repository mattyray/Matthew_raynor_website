from django.views.generic import DetailView, TemplateView, ListView
from .models import Product, Collection, Order, OrderItem
from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import ReviewForm  # Make sure this is at the top
from django.utils.decorators import method_decorator


import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def create_checkout_session(request):
    YOUR_DOMAIN = "https://www.matthewraynor.com"
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': 1000,  # 10.00 USD
                    'product_data': {
                        'name': 'Example Product',
                    },
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=YOUR_DOMAIN + '/order-success/',
        cancel_url=YOUR_DOMAIN + '/store/',
    )
    return JsonResponse({'id': checkout_session.id})



@method_decorator(login_required, name='dispatch')
class OrderHistoryView(ListView):
    model = Order
    template_name = 'store/order_history.html'
    context_object_name = 'orders'
    ordering = ['-created_at']

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderSuccessView(TemplateView):
    template_name = "store/order_success.html"

@require_POST
def remove_from_cart(request, key):
    cart = Cart(request)
    cart.remove(key)
    messages.success(request, "Item removed from your cart.")
    return redirect("store:cart_detail")

@login_required
@require_POST
def checkout_view(request):
    cart = Cart(request)
    if not cart.cart:
        messages.error(request, "Your cart is empty.")
        return redirect("store:cart_detail")

    order = Order.objects.create(user=request.user)
    print("DEBUG CART CONTENTS:", cart.cart)

    for key, item in cart.cart.items():
        product = Product.objects.get(id=key)
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=item["quantity"],
            price=product.price,
        )

    cart.clear()
    messages.success(request, "Your order has been placed successfully.")
    return redirect("store:order_success")

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.add(product)
    return redirect("store:cart_detail")

def cart_detail(request):
    cart = Cart(request)
    return render(request, "store/cart_detail.html", {"cart": cart})


class ProductDetailView(DetailView):
    model = Product
    template_name = "store/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['form'] = ReviewForm()
        context['reviews'] = product.reviews.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = self.object
            review.user = request.user
            review.save()
            messages.success(request, "Thank you for your review!")
            return redirect("store:product_detail", slug=self.object.slug)
        else:
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)

class CollectionDetailView(DetailView):
    model = Collection
    template_name = "store/collection_detail.html"
    context_object_name = "collection"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artworks'] = Product.objects.filter(
            product_type='artwork', 
            collection=self.object
        )
        return context

class StoreOverviewView(TemplateView):
    template_name = "store/store_overview.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Product.objects.filter(product_type='book')
        context['collections'] = Collection.objects.all()
        return context
    

