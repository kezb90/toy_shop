from django.shortcuts import render
from django.shortcuts import render, redirect
from .cart import Cart
from product.models import Product

def add_to_cart(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(pk=product_id)
    cart.add_product(product_id, quantity=1)
    return redirect('product_list')  # Redirect to your product list or wherever you want after adding to the cart

def view_cart(request):
    cart = Cart(request)
    cart_items = []
    total_price = 0

    for product_id, item in cart.cart.items():
        product = Product.objects.get(pk=product_id)
        total_price += product.price * item['quantity']
        cart_items.append({'product': product, 'quantity': item['quantity']})

    return render(request, 'view_cart.html', {'cart_items': cart_items, 'total_price': total_price})
