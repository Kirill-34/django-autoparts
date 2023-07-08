from django.contrib import admin

from products.models import ProductCategory, Brand, Specification, Product, Basket

admin.site.register(ProductCategory)
admin.site.register(Brand)
admin.site.register(Specification)
admin.site.register(Basket)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'article', 'image_main', ('image_1', 'image_2', 'image_3'), ('price', 'quantity'), 'description', 'category', 'brand', 'specification')
    ordering = ('name',)
    search_fields = ('name',)
