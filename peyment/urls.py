from django.urls import path, include
from .views import peyment, resault

app_name = "peyment"
urlpatterns = [
    path("peyment_page/", peyment, name="payment-page"),
    path("peyment_resault/<int:is_paid>/", resault, name="resault"),
]
