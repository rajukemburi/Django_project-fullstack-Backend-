from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from orders.models import Order
from products.models import Product
from django.db.models import Sum

@staff_member_required
def dashboard_home(request):
    total_orders = Order.objects.count()
    total_sales = Order.objects.aggregate(total=Sum('total_price'))['total'] or 0
    total_products = Product.objects.count()
    context = {
        'total_orders': total_orders,
        'total_sales': total_sales,
        'total_products': total_products,
    }
    return render(request, 'dashboard/home.html', context)
