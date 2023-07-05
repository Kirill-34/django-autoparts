from django.contrib import admin
from django.urls import path

from products.views import index, products, product, search_res, basket_add, basket_delete, basket_item_inc, basket_item_dec, contact

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:category_id>/', products, name='index_cat'),
    path('brand/<int:brand_id>/', products, name='index_brand'),
    path('page/<int:page>/', products, name='page'),
    path('search_res/', search_res, name='search_res'),
    path('product/<int:product_id>/', product, name='product'),
    path('basket-add/<int:product_id>', basket_add, name='basket_add'),
    path('basket-delete/<int:id>', basket_delete, name='basket_delete'),
    path('basket-item-inc/<int:product_id>', basket_item_inc, name='basket_item_inc'),
    path('basket-item-dec/<int:product_id>', basket_item_dec, name='basket_item_dec'),
    path('contact/', contact, name='contact'),
]