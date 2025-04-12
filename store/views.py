from django.views.generic import DetailView, TemplateView
from .models import Product, Collection
from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.add(product)
    return redirect("store:cart_detail")


def cart_detail(request):
    cart = Cart(request)
    return render(request, "store/cart_detail.html", {"cart": cart})

#--


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
        # Only include artwork products in this collection
        context['artworks'] = Product.objects.filter(
            product_type='artwork', 
            collection=self.object
        )
        return context

class StoreOverviewView(TemplateView):
    template_name = "store/store_overview.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch books (products with product_type 'book')
        context['books'] = Product.objects.filter(product_type='book')
        # Fetch all artwork collections
        context['collections'] = Collection.objects.all()
        return context
