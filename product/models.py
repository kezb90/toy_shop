from django.db import models
from ckeditor.fields import RichTextField
from blog.models import MyBaseModel

# Create your models here.


class Category(MyBaseModel):
    name = models.CharField(max_length=255, unique=True)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.name


class Product(MyBaseModel):
    name = models.CharField(max_length=255)
    description = RichTextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class ProductImage(MyBaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_images/")
    alt = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.alt
