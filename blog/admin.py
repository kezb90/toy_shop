from django.contrib import admin
from django.contrib.admin import register

# Register your models here.
from .models import Post, Category, Comment, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "is_active",
        "created_at",
        "updated_at",
    )
    list_display_links = ("id", "title")
    search_fields = ("title", "description")


@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "body", "is_active", "created_at", "updated_at")
    list_display_links = ("id", "title")
    search_fields = ("title",)
    inlines = [CommentInline]


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "is_active",
        "created_at",
        "updated_at",
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
        "updated_at",
    )
    list_display_links = ("id", "author")
    search_fields = ("title", "body", "author", "description")
