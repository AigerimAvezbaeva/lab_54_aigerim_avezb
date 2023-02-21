from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from products_app.models import Product
from products_app.models import Category


def products_index(request: WSGIRequest):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products_index.html', context=context)


def categories_index(request: WSGIRequest):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories_index.html', context=context)
