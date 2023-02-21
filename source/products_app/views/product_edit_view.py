from django.shortcuts import get_object_or_404, render
from products_app.forms import ProductForm
from products_app.models import Category


def product_edit_view(request, pk):
    product = get_object_or_404(Category, pk=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid:
            form.save()
            return render(request, 'products_index.html')
    context = {
        'form': form,
        'product': product
    }
    return render(request, 'edit_product.html', context=context)
