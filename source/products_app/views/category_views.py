from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from products_app.models import Category
from products_app.forms import CategoryForm


def category_view(request: WSGIRequest):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories_index.html', context=context)


def add_category(request: WSGIRequest):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories/')
    return render(request, 'add_category.html', context={
        'form': form
    })


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories_index.html', context=context)


def category_edit_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid:
            form.save()
            return render(request, 'categories_index.html')
    context = {
        'form': form,
        'category': category
    }
    return render(request, 'edit_category.html', context=context)
