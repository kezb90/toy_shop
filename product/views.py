from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "product_detail.html", {"product": product})


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "product_list.html", context)
