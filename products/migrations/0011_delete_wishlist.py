# Generated by Django 4.2.1 on 2023-06-15 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_in_wishlist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WishList',
        ),
    ]