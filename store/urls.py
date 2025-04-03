from django.urls import path
from .views import (
    ProductDetailView,
    CollectionDetailView,
    StoreOverviewView,
)

urlpatterns = [
    # New store overview page as the root for the store app:
    path('', StoreOverviewView.as_view(), name='store_overview'),
    # Additional URL patterns:
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('collections/<slug:slug>/', CollectionDetailView.as_view(), name='collection_detail'),
]
