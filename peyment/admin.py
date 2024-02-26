from django.contrib import admin
from django.contrib.admin import register

from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "status",
        "total_price",
        "created_at",
        "updated_at",
        "is_active",
    )
    list_display_links = ("id",)
    search_fields = ("user__username",)
    inlines = [
        OrderItemInline,
    ]


@register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order",
        "product",
        "quantity",
        "unit_price",
        "item_price",
        "created_at",
        "updated_at",
        "is_active",
    )
    list_display_links = ("id",)
    search_fields = (
        "product__name",
        "order__id",
    )
    

