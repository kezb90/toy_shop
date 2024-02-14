from django.urls import path, include
from .views import main, about_us


urlpatterns = [
    path("", main, name="main"),
    path("about_us/", about_us, name="about_us"),
]
