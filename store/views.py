from django.views.generic import DetailView, TemplateView
from .models import Product, Collection, Order, OrderItem
from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages

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
    

