from django.urls import path, include
from rest_framework import routers
from .views import product_list


urlpatterns = [
    path('product_list/', product_list, name='product-list')
]
