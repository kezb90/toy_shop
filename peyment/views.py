from django.shortcuts import render
from shopping_basket.cart import Cart
from product.models import Product

# Create your views here.


def peyment(request):
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
    context = {"cart_items": cart_items, "total_price": total_price}
    return render(request, "peyment.html", context)


def resault(request, is_paid):
    if is_paid == 1:
        context = {"status_code": 1}
        return render(request, "resault.html", context)
    else:
        context = {"status_code": 0}
        return render(request, "resault.html", context)
