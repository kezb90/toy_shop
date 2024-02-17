from django.shortcuts import render
from .models import Category, Product
# Create your views here.

def product_list(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'product_list.html', context)
