# Generated by Django 4.2.1 on 2023-06-02 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='brand_images')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('API', models.CharField(blank=True, max_length=12)),
                ('ACEA', models.CharField(blank=True, max_length=12)),
                ('ILSAC', models.CharField(blank=True, max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('image', models.ImageField(blank=True, upload_to='products_images')),
                ('description', models.TextField(blank=True)),
                ('short_description', models.CharField(blank=True, max_length=64)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('brand', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='products.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.productcategory')),
                ('specification', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='products.specification')),
            ],
        ),
    ]