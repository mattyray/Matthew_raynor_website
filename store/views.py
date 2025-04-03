from django.views.generic import DetailView, TemplateView
from .models import Product, Collection

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
