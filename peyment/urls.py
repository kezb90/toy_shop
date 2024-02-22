from django.urls import path, include
from .views import peyment

app_name = "peyment"
urlpatterns = [
    path("peyment_page/", peyment, name="payment-page"),
]
