from django.contrib import admin
from .models import Product, Collection, Order, OrderItem, Review

# --------------------
# PRODUCT ADMIN
# --------------------
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'product_type', 'price', 'stock', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description')
    list_filter = ('created_at',)

# --------------------
# COLLECTION ADMIN
# --------------------
@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    prepopulated_fields = {'slug': ('name',)}

# --------------------
# ORDER ADMIN
# --------------------
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'created_at', 'total_price')
    list_filter = ('status', 'created_at')
    inlines = [OrderItemInline]

# --------------------
# REVIEW ADMIN
# --------------------
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('comment',)
