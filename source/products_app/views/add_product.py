from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from products_app.models import Product
from products_app.models import Category
from products_app.forms import ProductForm


def add_product(request: WSGIRequest):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'add_product.html', context={
        'form': form
    })


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={
        'product': product
    })
