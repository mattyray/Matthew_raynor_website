from django.views.generic import DetailView, TemplateView, ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


from .models import Product, Collection, Order, OrderItem
from .cart import Cart
from .forms import ReviewForm

import stripe
import json

stripe.api_key = settings.STRIPE_SECRET_KEY

from django.core.mail import send_mail
@csrf_exempt
def stripe_webhook(request):
    import logging
    logger = logging.getLogger(__name__)
    print("🔥 Webhook view hit")  # This should print if the view is entered
    logger.info("🔥 Webhook view hit")

    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', '')
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(
            payload=payload,
            sig_header=sig_header,
            secret=endpoint_secret,
        )
    except ValueError as e:
        print("❌ Invalid payload:", e)
        logger.error("❌ Invalid payload: %s", str(e))
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        print("❌ Signature verification failed:", e)
        logger.error("❌ Signature verification failed: %s", str(e))
        return HttpResponse(status=400)

    print(f"✅ Received Stripe event: {event['type']}")
    logger.info(f"✅ Received Stripe event: {event['type']}")

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        customer_email = session.get('customer_email') or session.get("customer_details", {}).get("email")
        shipping_name = session.get('shipping', {}).get('name') or session.get("customer_details", {}).get("name")
        shipping_address = session.get('shipping', {}).get('address') or session.get("customer_details", {}).get("address")

        email_body = f"""
        ✅ New Order Completed!

        Customer: {customer_email}
        Name: {shipping_name}
        Address: {shipping_address}
        """

        print(email_body)
        logger.info(email_body)

        send_mail(
            subject="📦 New Order Received",
            message=email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
        )

    return HttpResponse(status=200)



@csrf_exempt
def create_checkout_session(request):
    product_id = json.loads(request.body).get("product_id")
    product = Product.objects.get(id=product_id)

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': int(product.price * 100),
                    'product_data': {
                        'name': product.title,
                    },
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=settings.DOMAIN + '/store/order_success/',
        cancel_url=settings.DOMAIN + '/store/',
        shipping_address_collection={'allowed_countries': ['US', 'CA']},
        metadata={'product_id': product.id, 'user_id': request.user.id}
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

    line_items = []
    for key, item in cart.cart.items():
        product = Product.objects.get(id=key)
        line_items.append({
            'price_data': {
                'currency': 'usd',
                'unit_amount': int(float(product.price) * 100),  # price in cents
                'product_data': {
                    'name': product.title,
                },
            },
            'quantity': item["quantity"],
        })

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        shipping_address_collection={'allowed_countries': ['US']},
        success_url=request.build_absolute_uri('/store/order_success/'),
        cancel_url=request.build_absolute_uri('/cart/'),
    )

    return redirect(checkout_session.url)

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
        context['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY  # ✅ required for frontend JS
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
