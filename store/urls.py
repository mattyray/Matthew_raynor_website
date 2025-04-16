from django.urls import path
from .views import (
    ProductDetailView,
    CollectionDetailView,
    StoreOverviewView,
    cart_detail,
    add_to_cart,
    checkout_view,
    OrderSuccessView,
    remove_from_cart,
    OrderHistoryView
)

app_name = "store"

urlpatterns = [
    path('', StoreOverviewView.as_view(), name='store_overview'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('collections/<slug:slug>/', CollectionDetailView.as_view(), name='collection_detail'),

    # Cart functionality
    path("cart/", cart_detail, name="cart_detail"),
    path("cart/add/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path("cart/remove/<str:key>/", remove_from_cart, name="remove_from_cart"),  # ✅ This line is key

    path("checkout/", checkout_view, name="checkout"),
    path("order-success/", OrderSuccessView.as_view(), name="order_success"),
    path('orders/history/', OrderHistoryView.as_view(), name='order_history'),
   
]
