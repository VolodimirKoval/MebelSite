# Generated by Django 4.2.6 on 2024-05-29 06:50

from django.db import migrations, models
import django.db.models.deletion
import shop.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=120, unique=True, verbose_name='Назва категорії')),
                ('slug', models.SlugField(max_length=120, unique=True, verbose_name='URL категорії')),
            ],
            options={
                'verbose_name': 'категорія',
                'verbose_name_plural': 'Категорії',
                'db_table': 'categories',
                'ordering': ['category_name'],
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=160, unique=True, verbose_name='Назва продукту')),
                ('slug', models.SlugField(max_length=160, unique=True, verbose_name='URL продукту')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Опис продукту')),
                ('image', models.ImageField(blank=True, null=True, upload_to=shop.models.auto_image_folder, verbose_name='Фото')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Ціна')),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Знижка')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Кількість')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Категорія')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'Продукти',
                'db_table': 'products',
                'ordering': ['category', 'product_name'],
            },
        ),
    ]