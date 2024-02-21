from django.db import models
from blog.models import MyBaseModel
from product.models import Product


class Order(MyBaseModel):
    is_paid = models.BooleanField(default=False)
    first_name = models.CharField(max_length=150, null=False, blank=False)
    last_name = models.CharField(max_length=150, null=False, blank=False)
    address = models.TextField()
    phone = models.CharField(max_length=15, null=False, blank=False)


class ItemOrder(MyBaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, null=False, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(null=False, blank=False)

    @property
    def unit_price(self):
        return self.product.price

    @property
    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name
