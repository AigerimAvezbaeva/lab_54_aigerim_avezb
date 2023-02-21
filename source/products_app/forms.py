from django.forms import ModelForm
from django.http import request
from django.shortcuts import get_object_or_404

from products_app.models import Category, Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
