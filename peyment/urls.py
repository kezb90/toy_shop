from django.urls import path, include
from .views import peyment, resault, create_order, OrderView

app_name = "peyment"
urlpatterns = [
    path("peyment_page/<int:order_id>", peyment, name="payment-page"),
    path("peyment_resault/<int:is_paid>/<int:order_id>/", resault, name="resault"),
    path("create_order/", create_order, name="create-order"),
    path("order_list/", OrderView.as_view(), name="order-list"),
]
