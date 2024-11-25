from django.contrib import admin
from .models import Category, SubCategory, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'stock', 'sub_category', 'created_at')  # updated 'category' to 'sub_category'
    list_filter = ('sub_category',)  # updated 'category' to 'sub_category'

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'created_at')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at')

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
