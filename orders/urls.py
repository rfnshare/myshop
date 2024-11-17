from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_order, name='create_order'),  # Create a new order
    path('list/', views.list_orders, name='list_orders'),      # List all orders for the user
    path('<int:order_id>/', views.order_detail, name='order_detail'),  # View order details
    path('<int:order_id>/update/', views.update_order, name='update_order'),  # Update order status
    path('<int:order_id>/delete/', views.delete_order, name='delete_order'),  # Delete an order
]
