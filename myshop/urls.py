"""
URL configuration for myshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Mobile Sales API",
        default_version='v1',
        description="API documentation for the mobile sales system",
        contact=openapi.Contact(email="contact@mobile.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[AllowAny],  # Allow any user to access Swagger UI
)

urlpatterns = [
    path('swagger/', schema_view.as_view(), name='swagger'),
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
    path('products/', include('products.urls')),  # Placeholder for products URLs
    path('orders/', include('orders.urls')),      # Placeholder for orders URLs
    path('users/', include('users.urls')),        # Placeholder for user management URLs
]