from django.urls import path

from products_app.views.base import products_index
from products_app.views.add_product import add_product, product_view
from products_app.views.delete_product import delete_product
from products_app.views.category_views import category_view, add_category, delete_category, category_edit_view
from products_app.views.product_edit_view import product_edit_view

urlpatterns = [
    path('', products_index, name='index'),
    path('products/', products_index),
    path('products/add/', add_product, name='add_product'),
    path('products/<int:pk>', product_view, name='product_detail'),
    path('products/<str:pk>/edit', product_edit_view, name='edit_product'),
    path('products/delete/<int:pk>', delete_product, name='delete_product'),
    path('categories/', category_view, name='category_index'),
    path('categories/categories/', category_view, name='category_index'),
    path('categories/add', add_category, name='add_category'),
    path('categories/delete/<int:pk>', delete_category, name='delete_category'),
    path('categories/<str:pk>/edit', category_edit_view, name='edit_category')
]
