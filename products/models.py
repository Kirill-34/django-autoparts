from django.db import models

from users.models import User

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='productcategories_images', blank=True)

    class Meta:
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=64, unique=True)
    image = models.ImageField(upload_to='brand_images', blank=True)

    def __str__(self):
        return self.name

class Specification(models.Model):
    API = models.CharField(max_length=12, blank=True)
    ACEA = models.CharField(max_length=12, blank=True)
    ILSAC = models.CharField(max_length=12, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=256)
    image_main = models.ImageField(upload_to='products_images', blank=True)
    image_1 = models.ImageField(upload_to='products_images', blank=True)
    image_2 = models.ImageField(upload_to='products_images', blank=True)
    image_3 = models.ImageField(upload_to='products_images', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    article = models.CharField(max_length=30, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)
    created_date = models.DateField(auto_now_add=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True)
    specification = models.ForeignKey(Specification, on_delete=models.SET_NULL, blank=True, null=True)
    in_wishlist = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} | {self.category.name}'

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Заказ для {self.user.username} | Сумма {self.basket.sum()} руб.'

