# Generated by Django 3.2.6 on 2021-08-25 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_products_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
