from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # Serialize all fields

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Include nested serializer for category

    class Meta:
        model = Product
        fields = '__all__'  # Serialize all fields
