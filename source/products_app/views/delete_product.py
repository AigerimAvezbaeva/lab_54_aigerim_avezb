from django.shortcuts import render, get_object_or_404

from products_app.models import Product


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products_index.html', context=context)

