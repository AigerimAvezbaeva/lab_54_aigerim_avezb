from django.contrib import admin
from products_app.models import Product, Category


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price')
    list_filter = ('id', 'name', 'category', 'created_at')
    search_fields = ('name', 'category', 'price')
    list_editable = ['price']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_filter = ('id', 'title')
    search_fields = ('id', 'title')
    list_editable = ('title', 'description')
    list_display_links = ['id']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
