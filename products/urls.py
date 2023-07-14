from django.contrib import admin
from django.urls import path

from products import views

app_name = 'products'

urlpatterns = [
    path('', views.products, name='index'),
    path('category/<int:category_id>/', views.products, name='index_cat'),
    path('category/<int:category_id>/page/<int:page>/', views.products, name='index_cat_page'),
    path('brand/<int:brand_id>/', views.products, name='index_brand'),
    path('brand/<int:brand_id>/page/<int:page>/', views.products, name='index_brand_page'),
    path('page/<int:page>/', views.products, name='page'),
    path('search_res/', views.search_res, name='search_res'),
    path('product/<int:product_id>/', views.product, name='product'),
    path('basket-add/<int:product_id>', views.basket_add, name='basket_add'),
    path('basket-delete/<int:id>', views.basket_delete, name='basket_delete'),
    path('basket-item-inc/<int:product_id>', views.basket_item_inc, name='basket_item_inc'),
    path('basket-item-dec/<int:product_id>', views.basket_item_dec, name='basket_item_dec'),
    path('order-add/', views.order_add, name='order_add'),
    path('question/', views.question, name='question'),
    path('order-question/', views.order_question, name='order_question'),
    path('return/', views.return_good, name='return'),
    path('about-order/', views.about_order, name='about_order'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('contact-question/', views.contact_question, name='contact_question'),
]