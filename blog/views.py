from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Category, Post, Comment

# Create your views here.


# Represent landing page
def main(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "main.html", context)


# Represent about us page
def about_us(request):
    return render(request, "about_us.html")


def category_posts_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = category.posts.filter(is_active=True)

    context = {
        "posts": posts,
    }

    return render(request, "category_posts.html", context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # This fetches all comments associated with the post
    # comments = post.comment_set.filter(is_active=True)
    comments = Comment.objects.filter(post=post, is_active=True).order_by("-created_at")
    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "post_detail.html", context)


def search_view(request):
    query = request.GET.get("q")
    if query or query == "":
        # Perform a simple case-insensitive search on the Post title and body
        posts = Post.objects.filter(is_active=True, title__icontains=str(query))

    else:
        posts = []
    context = {
        "posts": posts,
    }
    return render(request, "category_posts.html", context)


def comment_view(request, post_id):
    if request.method == "POST":
        # Retrieve data from the form
        author = request.POST.get("author", "")
        comment_text = request.POST.get("comment", "")

        # Perform any necessary validation here

        # Create a new Comment instance and save it to the database
        comment = Comment(
            author=author, body=comment_text, post=Post.objects.get(id=post_id)
        )
        comment.save()

        # Redirect to a success page or the same page with a success message
        return redirect(reverse("post_detail", args=[post_id]))

    # If the request method is not POST, handle accordingly (e.g., show the form)
    # Replace 'your_template_name.html' with your actual template file
    return render(request, "your_template_name.html")
    context = {
        "post": post,
        "comments": comments,
    }
    return render(request, "post_detail.html", context)
