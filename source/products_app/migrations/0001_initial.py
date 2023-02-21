# Generated by Django 4.1.6 on 2023-02-17 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400, verbose_name='Наименование категории')),
                ('description', models.TextField(max_length=3000, null=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, verbose_name='Наименование')),
                ('description', models.TextField(max_length=3000, null=True, verbose_name='Описание')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Время создания')),
                ('price', models.DecimalField(decimal_places=3, max_digits=100, verbose_name='Цена')),
                ('photo', models.URLField(max_length=1000, verbose_name='Ссылка на картинку')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='category', to='products_app.category', verbose_name='Категория')),
            ],
        ),
    ]