from django.db import models
from ckeditor.fields import RichTextField
from blog.models import MyBaseModel
from django.db.models import Max
from django.contrib.auth.models import User

# Create your models here.


class Category(MyBaseModel):
    name = models.CharField(max_length=255, unique=True)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.name


class Product(MyBaseModel):
    name = models.CharField(max_length=255)
    description = RichTextField(blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def price(self):
        last_price = self.prices.aggregate(last_created=Max("created_at"))[
            "last_created"
        ]
        if last_price:
            return self.prices.filter(created_at=last_price).first().amount
        return None


class Price(MyBaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="prices"
    )
    amount = models.PositiveIntegerField(null=False, blank=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.product.name


class Image(MyBaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="product_images/")
    description = RichTextField()

    def __str__(self):
        return self.title


class Video(MyBaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="videos"
    )
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to="product_videos/")
    description = RichTextField()

    def __str__(self):
        return self.title


class Audio(MyBaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="audios"
    )
    title = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to="product_audios/")
    description = RichTextField()

    def __str__(self):
        return self.title


class Comment(MyBaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Comment by {self.user.username} on {self.product.name}"
