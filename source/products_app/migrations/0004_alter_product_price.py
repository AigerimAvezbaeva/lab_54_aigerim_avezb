# Generated by Django 4.1.6 on 2023-02-19 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0003_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=11, verbose_name='Цена'),
        ),
    ]
