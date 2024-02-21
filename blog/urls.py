from django.urls import path, include
from .views import main, about_us, comment_view, category_posts_view, post_detail
from rest_framework import routers
from .views import CategoryViewSet, ImageViewSet, GalleryView

category_router = routers.DefaultRouter()
category_router.register(
    "",
    CategoryViewSet,
)

image_router = routers.DefaultRouter()
image_router.register(r"images", ImageViewSet)
app_name = "blog"
urlpatterns = [
    path("gallery/", GalleryView.as_view(), name="gallery"),
    path("image/", include(image_router.urls)),
    path("category", include(category_router.urls), name="category"),
    path("", main, name="main"),
    path("blog/", main, name="blog"),
    path("about_us/", about_us, name="about_us"),
    path("comment/<int:post_id>", comment_view, name="comment"),
    path("category/<int:category_id>/", category_posts_view, name="category_posts"),
    path("post/<int:post_id>/", post_detail, name="post_detail"),
]
