from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category, SubCategory, Product
from .serializers import CategorySerializer, SubCategorySerializer, ProductSerializer, CategoryNestedSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class SubCategoryListCreateView(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class SubCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class HierarchicalProductView(APIView):
    def get(self, request, *args, **kwargs):
        # Fetch categories with related subcategories and products
        categories = Category.objects.prefetch_related('subcategory_set__product_set').all()

        # Serialize categories, subcategories, and products
        category_data = []
        for category in categories:
            subcategories = []
            for subcategory in category.subcategory_set.all():
                products = Product.objects.filter(sub_category=subcategory)
                product_data = ProductSerializer(products, many=True, context={'request': request}).data
                subcategories.append({
                    'id': subcategory.id,
                    'name': subcategory.name,
                    'products': product_data
                })
            category_data.append({
                'id': category.id,
                'name': category.name,
                'image': request.build_absolute_uri(category.image.url) if category.image else None,
                'subCategories': subcategories
            })

        return Response({'categories': category_data})
