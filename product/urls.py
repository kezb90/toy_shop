from django.urls import path, include
from rest_framework import routers
from .views import product_list, product_detail

app_name = "product"
urlpatterns = [
    path("detail/<int:product_id>", product_detail, name="detail"),
    path("product_list/", product_list, name="product-list"),
]
