# Generated by Django 4.2 on 2023-04-26 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_marca_product_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]
