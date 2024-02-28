from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from shopping_basket.cart import Cart
from product.models import Product
from .models import Order, OrderItem
from product.models import Product
from shopping_basket.cart import Cart
from rest_framework.generics import ListAPIView
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class OrderView(ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        # Filter the queryset to show only orders of the authenticated user
        return Order.objects.filter(user=self.request.user)


def peyment(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    total_price = order.total_price
    order_items = order.order_items.all()

    context = {
        "total_price": total_price,
        "order_id": order.pk,
        "user_name": order.user.username,
        "order_items": order_items,
    }
    return render(request, "peyment.html", context)


def resault(request, is_paid, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if is_paid == 1:
        order.is_paid = True
        order.status = "pending"
        order.save()

    else:
        order.is_paid = False
        order.status = "failed"
        order.save()

    context = {
        "status": order.status,
        "is_paid": order.is_paid,
        "total_price": order.total_price,
    }
    return render(request, "resault.html", context)


def create_order(request):
    if request.method == "GET":
        # Get or create the user's cart
        cart = Cart(request)
        # Create order
        order = Order.objects.create(
            is_active=True,
            user=request.user,  # Assuming you have authentication
            status="checkout",  # Set the appropriate status
            is_paid=False,
        )
        # Save the order
        order.save()
        for product_id, item in cart.cart.items():
            # Retrieve the product
            product = Product.objects.get(pk=product_id)
            quantity = item["quantity"]

            # Create OrderItem
            order_item = OrderItem.objects.create(
                is_active=True,
                order=order,  # You will update this with the actual order instance
                product=product,
                quantity=quantity,
            )

            # You may want to update additional fields such as shipping address, payment method, etc.
            # Save the order_item
            order_item.save()

        # Clear the session for cart
        cart.clear()

        # Construct the URL for the payment page
        payment_page_url = reverse("peyment:payment-page", args=[order.pk])

        # Redirect to the payment page
        return redirect(payment_page_url)
    else:
        return redirect("order-list")
