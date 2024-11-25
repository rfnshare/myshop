from rest_framework import serializers
from .models import Category, SubCategory, Product

class CategorySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at', 'image', 'image_url']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None

class SubCategorySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True) # UUID field for subcategory

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'description', 'category', 'created_at']

class ProductSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True) # UUID field for product
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'category', 'sub_category', 'image', 'image_url', 'created_at']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None

class ProductNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'image']  # Include only necessary fields

class SubCategoryNestedSerializer(serializers.ModelSerializer):
    products = ProductNestedSerializer(many=True, read_only=True, source='product_set')

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'products']  # Include subcategory details and associated products

class CategoryNestedSerializer(serializers.ModelSerializer):
    subCategories = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'subCategories']
