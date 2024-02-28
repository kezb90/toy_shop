from django.urls import path, include
from rest_framework import routers
from .views import product_list, product_detail, ProductDetailsView

app_name = "product"
urlpatterns = [
    path(
        "product_details/<int:pk>/",
        ProductDetailsView.as_view(),
        name="product-details",
    ),
    path("", product_list, name="product-list"),
]
