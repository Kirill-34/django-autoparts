# Generated by Django 4.2.1 on 2023-07-06 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]