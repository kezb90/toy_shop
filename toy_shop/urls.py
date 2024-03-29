"""
URL configuration for toy_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = (
    [
        path(settings.ADMIN_URL, admin.site.urls, name="admin"),
        path("", include("blog.urls", namespace="blog")),
        path("accounts/", include("accounts.urls", namespace="accounts")),
        path("product/", include("product.urls", namespace="product")),
        path(
            "shopping_basket/",
            include("shopping_basket.urls", namespace="shopping_basket"),
        ),
        path("peyment/", include("peyment.urls", namespace="peyment")),
        path("api-auth/", include("rest_framework.urls")),
        path("ckeditor/", include("ckeditor_uploader.urls")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
