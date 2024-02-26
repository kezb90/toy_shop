from django.shortcuts import render, redirect
from shopping_basket.cart import Cart
from product.models import Product
from .models import Order, OrderItem
from product.models import Product
from shopping_basket.cart import Cart

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


def create_order(request):
    if request.method == "GET":
        # Get or create the user's cart
        cart = Cart(request)
        # Create order
        order = Order.objects.create(
            user=request.user,  # Assuming you have authentication
            status="pending",  # Set the appropriate status
        )
        # Save the order
        order.save()
        for product_id, item in cart.cart.items():
            # Retrieve the product
            product = Product.objects.get(pk=product_id)
            quantity = item["quantity"]

            
            # Create OrderItem
            order_item = OrderItem.objects.create(
                order=order,  # You will update this with the actual order instance
                product=product,
                quantity=quantity,
            )

            # You may want to update additional fields such as shipping address, payment method, etc.
            # Save the order_item
            order_item.save()

            # Clear the cart
        cart.clear()
        return redirect("peyment:payment-page")  # Redirect to a peyment page
