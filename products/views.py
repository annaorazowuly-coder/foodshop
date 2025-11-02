from django.shortcuts import render
from .models import Product, products_for_sale  # İkisini de import et

def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})

def category_view(request, category_name):
    products = Product.objects.filter(category=category_name)
    sale_products = products_for_sale.objects.all()    
    return render(request, 'products/category_view.html', {
        'products': products,          
        'sale_products': sale_products, 
        'category_name': category_name
    })
