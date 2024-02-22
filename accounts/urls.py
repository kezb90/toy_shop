from django.urls import path
from .views import user_register, login_view, logout_view

app_name = "accounts"
urlpatterns = [
    path("user_register/", user_register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
