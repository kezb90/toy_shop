from django.urls import path, include
from .views import main, about_us, comment_view, category_posts_view, post_detail


urlpatterns = [
    path("", main, name="main"),
    path("blog/", main, name="blog"),
    path("about_us/", about_us, name="about_us"),
    path("comment/<int:post_id>", comment_view, name="comment"),
    path("category/<int:category_id>/", category_posts_view, name="category_posts"),
    path("post/<int:post_id>/", post_detail, name="post_detail"),
]
