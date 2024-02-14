from django.contrib import admin
from django.contrib.admin import register

# Register your models here.
from .models import Post, Category, Comment


@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "body", "is_active", "created_at", "modified_at")
    list_display_links = ("id",)
    search_fields = ("title",)


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "is_active",
        "created_at",
        "modified_at",
    )
    list_display_links = ("id", "title")
    search_fields = ("title", "description")


@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "body",
        "post",
        "is_active",
        "created_at",
        "modified_at",
    )
    list_display_links = ("id", "author")
    search_fields = ("title", "body", "author", "description")
