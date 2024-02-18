from django.urls import path, include
from rest_framework import routers
from .views import product_list

app_name = 'product'
urlpatterns = [
    path('product_list/', product_list, name='product-list')
]
