from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=400, blank=False, null=False, verbose_name='Наименование категории')
    description = models.TextField(max_length=3000, blank=False, null=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=400, blank=False, null=False, verbose_name='Наименование')
    description = models.TextField(max_length=3000, blank=False, null=True, verbose_name='Описание')
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        null=False,
        blank=False,
        related_name='category',
        on_delete=models.PROTECT)

    created_at = models.DateField(auto_now_add=True, verbose_name="Время создания")
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Цена')
    photo = models.URLField(null=True, verbose_name='Ссылка на изображение')

    def __str__(self):
        return f'{self.name} - {self.price}'
