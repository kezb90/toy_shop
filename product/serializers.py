from rest_framework import serializers
from .models import Product, Category, Price
from django.db.models import Max


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField(read_only=True)
    # category = CategorySerializer(many=False)

    class Meta:
        model = Product
        fields = "__all__"

    def get_price(self, obj):
        last_price = obj.prices.aggregate(last_created=Max("created_at"))[
            "last_created"
        ]
        if last_price:
            return obj.prices.filter(created_at=last_price).first().amount
        return None
