from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q


def product_list(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    products = Product.objects.all()
    if category:
        products = products.filter(category__slug=category)
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    categories = Category.objects.all()
    return render(request, 'products/product_list.html', {'products': products, 'categories': categories})




def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'products/product_detail.html', {'product': product})