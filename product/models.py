from django.db import models
from ckeditor.fields import RichTextField
from blog.models import MyBaseModel
from django.db.models import F, Max
# Create your models here.


class Category(MyBaseModel):
    name = models.CharField(max_length=255, unique=True)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.name


class Product(MyBaseModel):
    name = models.CharField(max_length=255)
    description = RichTextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    @property
    def price(self):
        last_price = self.prices.aggregate(last_created=Max('created_at'))['last_created']
        if last_price:
            return self.prices.filter(created_at=last_price).first().amount
        return None
        

class Price(MyBaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices')
    amount = models.PositiveIntegerField(null=False, blank=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.product.name
    
class ProductImage(MyBaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_images/")
    alt = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.alt
