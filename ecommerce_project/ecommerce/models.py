from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model for the eCommerce application.
    Users can register as vendors or buyers.
    """

    USER_ROLES = [
        ('vendor', 'Vendor'),
        ('buyer', 'Buyer'),
    ]

    role = models.CharField(
        max_length=10,
        choices=USER_ROLES,
        default='buyer'
    )

    def __str__(self):
        return f"{self.username} - {self.role}"

# Create your models here.
class Store(models.Model):
    """
    Stores created and managed by vendors.
    """

    vendor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='stores'
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    
class Product(models.Model):
    """
    Products listed for sale in a vendor's store.
    """

    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name='products'
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class Order(models.Model):
    """
    Records orders placed by buyers.
    """

    ORDER_STATUS = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]

    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )
    status = models.CharField(
        max_length=10,
        choices=ORDER_STATUS,
        default='pending'
    )

    def __str__(self):
        return f"Order {self.id} - {self.buyer.username}"

class OrderItem(models.Model):
    """
    Records individual products included in an order.
    """

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    product_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.product_name} - {self.quantity}"

class Review(models.Model):
    """
    Stores reviews submitted by buyers for products.
    """

    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.PositiveSmallIntegerField(
        choices=[
            (1, '1 Star'),
            (2, '2 Stars'),
            (3, '3 Stars'),
            (4, '4 Stars'),
            (5, '5 Stars'),
        ]
    )
    comment = models.TextField()
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.buyer.username} for {self.product.name}"
    
