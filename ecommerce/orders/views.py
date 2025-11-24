from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from .models import Order, OrderItem
from django.contrib import messages

@login_required
def checkout(request):
    items = CartItem.objects.filter(user=request.user)
    if not items:
        messages.error(request, 'Your cart is empty.')
        return redirect('product-list')

    total = sum([item.subtotal() for item in items])
    # Create Order
    order = Order.objects.create(user=request.user, total_price=total)
    for item in items:
        OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity, price=item.product.price)
        # optionally reduce stock
        item.product.stock = max(item.product.stock - item.quantity, 0)
        item.product.save()
    # clear cart
    items.delete()
    messages.success(request, 'Order placed successfully.')
    return redirect('order-detail', order_id=order.id)

@login_required
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})

