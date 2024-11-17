from django.http import JsonResponse
from .models import Order, OrderItem
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json

# Create a new order
@csrf_exempt
def create_order(request):
    if request.method == "POST":
        data = json.loads(request.body)
        # Assuming `data` contains user and items info
        user = request.user
        total_price = sum(item['price'] * item['quantity'] for item in data['items'])
        order = Order.objects.create(user=user, total_price=total_price)
        for item in data['items']:
            OrderItem.objects.create(
                order=order,
                product_id=item['product_id'],  # Use product ID to fetch the product
                quantity=item['quantity']
            )
        return JsonResponse({'message': 'Order created successfully!', 'order_id': order.id})

# List all orders for the logged-in user
def list_orders(request):
    user = request.user
    orders = Order.objects.filter(user=user).values()
    return JsonResponse(list(orders), safe=False)

# View order details
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    items = order.items.all().values('product__name', 'quantity', 'product__price')
    order_data = {
        'id': order.id,
        'total_price': order.total_price,
        'status': order.status,
        'items': list(items),
    }
    return JsonResponse(order_data)

# Update an order (e.g., status)
@csrf_exempt
def update_order(request, order_id):
    if request.method == "POST":
        order = get_object_or_404(Order, id=order_id, user=request.user)
        data = json.loads(request.body)
        if 'status' in data:
            order.status = data['status']
            order.save()
            return JsonResponse({'message': 'Order status updated successfully!'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

# Delete an order
@csrf_exempt
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order.delete()
    return JsonResponse({'message': 'Order deleted successfully!'})
