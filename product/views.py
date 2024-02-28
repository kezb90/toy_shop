from django.shortcuts import render, get_object_or_404
from .models import Product
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ProductSerializer
from .permissions import AdminOnlyPermission

# Create your views here.


class ProductDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.filter(is_active=True)
    permission_classes = [AdminOnlyPermission]
    serializer_class = ProductSerializer


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "product_detail.html", {"product": product})


def product_list(request):
    products = Product.objects.filter(is_active=True)
    context = {"products": products}
    return render(request, "product_list.html", context)
