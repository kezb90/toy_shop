from django.contrib import admin
from django.contrib.admin import register
from .models import Product, Category


@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "price", "stock", "created_at")
    list_display_links = ("id", "name")
    search_fields = ("name", "description")

@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    list_display_links = ("id", "name")
    search_fields = ("name", "description")
