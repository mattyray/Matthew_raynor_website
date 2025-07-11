from django.db import models
from django.conf import settings
from django.utils.text import slugify
from cloudinary_storage.storage import MediaCloudinaryStorage
from django.contrib.postgres.search import SearchVectorField  # ADD THIS
from django.contrib.postgres.indexes import GinIndex  # ADD THIS

User = settings.AUTH_USER_MODEL

class Product(models.Model):
    PRODUCT_TYPE_CHOICES = (
         ('book', 'Book'),
         ('artwork', 'Artwork'),
    )
    product_type = models.CharField(max_length=10, choices=PRODUCT_TYPE_CHOICES)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(
        upload_to='products/', 
        storage=MediaCloudinaryStorage(), 
        null=True, 
        blank=True
    )
    stock = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True)
    collection = models.ForeignKey(
        'Collection', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name="products"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # ADD THIS FIELD
    search_vector = SearchVectorField(null=True, blank=True)

    class Meta:
        # ADD THIS INDEX
        indexes = [
            GinIndex(fields=['search_vector']),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Order(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('F', 'Failed'),
    ]
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='orders', null=True, blank=True
    )
    customer_email = models.EmailField(null=True, blank=True)
    shipping_address = models.JSONField(null=True, blank=True)
    stripe_checkout_id = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())

    def __str__(self):
        return f"Order {self.id} ({self.customer_email or self.user})"



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.title}"


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=5)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review of {self.product.title} by {self.user}"


class Collection(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    cover_image = models.ImageField(
        upload_to='collections/', 
        storage=MediaCloudinaryStorage(), 
        null=True, 
        blank=True
    )
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name