from django.urls import path
from .views import (
    CategoryListCreateView, CategoryDetailView,
    SubCategoryListCreateView, SubCategoryDetailView,
    ProductListCreateView, ProductDetailView, HierarchicalProductView
)

urlpatterns = [
    # Category URLs
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<uuid:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    # SubCategory URLs
    path('subcategories/', SubCategoryListCreateView.as_view(), name='subcategory-list-create'),
    path('subcategories/<uuid:pk>/', SubCategoryDetailView.as_view(), name='subcategory-detail'),

    # Product URLs
    path('product/', ProductListCreateView.as_view(), name='product-list-create'),
    path('product/<uuid:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('products/hierarchical/', HierarchicalProductView.as_view(), name='hierarchical-products'),
]
