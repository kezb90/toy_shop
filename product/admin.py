from django.contrib import admin
from django.contrib.admin import register
from .models import Product, Category, Price

class ProductInline(admin.StackedInline):
    model = Product
    extra = 1

@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "is_active",
        "price",
        "stock",
        "created_at",
    )
    list_display_links = ("id", "name")
    search_fields = ("name", "description")
    

@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    list_display_links = ("id", "name")
    search_fields = ("name", "description")
    # inlines = [ProductInline]

@register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "is_active", "amount", "created_at")
    list_display_links = ("id", "product")
    search_fields = ("product", "ammount")
