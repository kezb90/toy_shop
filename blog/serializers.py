from rest_framework import serializers
from .models import Category, Post, Comment, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'title', 'image', 'description']
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('title', 'description',)

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Category` instance, given the validated data.
    #     """
    #     return Category.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Category` instance, given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.description = validated_data.get(
    #         'description', instance.description)
    #     instance.save()
    #     return instance
