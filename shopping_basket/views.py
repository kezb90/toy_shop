from django.shortcuts import render, redirect
from .cart import Cart
from product.models import Product
from django.contrib import messages


def add_to_cart(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(pk=product_id)
    cart.add_product(product_id, quantity=1)
    messages.success(
        request, "'{}' added to the Basket successfully!".format(product.name)
    )
    return redirect(
        "shopping_basket:view_cart"
    )  # Redirect to your product list or wherever you want after adding to the cart


def view_cart(request):
    cart = Cart(request)
    cart_items = []
    total_price = 0

    for product_id, item in cart.cart.items():
        try:
            product = Product.objects.get(pk=product_id)
            total_price += product.price * item["quantity"]
            cart_items.append(
                {
                    "product": product,
                    "quantity": item["quantity"],
                    "unit_price": product.price,
                    "sum": product.price * item["quantity"],
                }
            )
        except Product.DoesNotExist:
            print(cart.cart)
            cart.remove_product(product_id)
            cart.save()
            break
        except TypeError:
            cart.remove_product(product_id)
            cart.save()
            break

    return render(
        request,
        "view_cart.html",
        {"cart_items": cart_items, "total_price": total_price},
    )


def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    messages.success(request, "Buying Basket Successfully Cleared!")
    return render(request, "view_cart.html")
