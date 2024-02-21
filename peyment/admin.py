from django.contrib import admin
from django.contrib.admin import register

from .models import Order


# @register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = (
#         "id",
#         "product",
#         "unit_price",
#         "quantity",
#         "total_price",
#         "is_active",
#         "created_at",
#         "updated_at",
#     )
#     list_display_links = (
#         "id",
#         "product",
#     )
#     search_fields = ("product__name",)
