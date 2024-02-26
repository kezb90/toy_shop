from django.db import models
from blog.models import MyBaseModel
from product.models import Product
from django.contrib.auth.models import User


class Order(MyBaseModel):
    # Relationship with the user who placed the order
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    is_paid = models.BooleanField(default=False, null=False, blank=False)
    # Order status choices
    ORDER_STATUS_CHOICES = [
        ("checkout", "checkout"),
        ("failed", "failed"),
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("shipped", "Shipped"),
        ("delivered", "Delivered"),
        ("canceled", "Canceled"),
    ]

    # Status of the order (e.g., pending, shipped, delivered)
    status = models.CharField(
        max_length=20, choices=ORDER_STATUS_CHOICES, default="pending"
    )

    # Date and time when the order was created
    created_at = models.DateTimeField(auto_now_add=True)

    # Date and time when the order was last updated
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_total_price(self):
        # Calculate the total price based on the sum of item prices
        return sum(item.item_price for item in self.order_items.all())

    @property
    def total_price(self):
        # Use the calculate_total_price method as a property
        return self.calculate_total_price()

    # Additional fields, if needed, such as shipping address, payment method, etc.

    def __str__(self):
        return f"Order #{self.pk} - {self.user.username}"


class OrderItem(MyBaseModel):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_items"
    )
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()

    @property
    def unit_price(self):
        return self.product.price

    @property
    def item_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"Item #{self.pk} - {self.product.name} in Order #{self.order.pk}"
