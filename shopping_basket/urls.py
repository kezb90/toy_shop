from django.urls import path
from .views import add_to_cart, view_cart, clear_cart

app_name = "shopping_basket"
urlpatterns = [
    path("add_to_cart/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path("view_cart/", view_cart, name="view_cart"),
    path("clear_cart/", clear_cart, name="clear-cart"),
]
