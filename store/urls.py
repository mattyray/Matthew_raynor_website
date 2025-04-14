from django.urls import path
from .views import (
    ProductDetailView,
    CollectionDetailView,
    StoreOverviewView,
    cart_detail,
    add_to_cart,
    checkout_view,
    OrderSuccessView
)

app_name = "store"


urlpatterns = [
    # Store overview as the app homepage
    path('', StoreOverviewView.as_view(), name='store_overview'),
    
    # Product and Collection detail views
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('collections/<slug:slug>/', CollectionDetailView.as_view(), name='collection_detail'),
    
    # Cart functionality
    path("cart/", cart_detail, name="cart_detail"),
    path("cart/add/<int:product_id>/", add_to_cart, name="add_to_cart"),

    path("checkout/", checkout_view, name="checkout"),
    path("order-success/", OrderSuccessView.as_view(), name="order_success"),
]
