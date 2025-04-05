from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)  # Вложенные категории

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'image', 'price', 'stock', 'specifications', 'categories']