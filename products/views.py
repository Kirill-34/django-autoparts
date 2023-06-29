from django.shortcuts import render, HttpResponseRedirect, get_object_or_404

from django.contrib import auth

from products.models import ProductCategory, Brand, Specification, Product, Basket, Order
import datetime
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def index(request):
    if request.user == auth.models.AnonymousUser:
        total_quantity = 0
        total_sum = 0
    else:
        baskets = Basket.objects.filter(user=request.user)
        total_quantity = sum(basket.quantity for basket in baskets)
        total_sum = sum(basket.sum() for basket in baskets)

    context = {
        'title': 'Автосклад',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
        'brands': Brand.objects.all(),
        'news': (Product.objects.filter(created_date__gte=(datetime.date.today() - datetime.timedelta(days=7))) & Product.objects.filter(created_date__lte=(datetime.date.today()))),
        'new': Product.objects.all().order_by("-created_date")[:1],
        'total_sum': total_sum,
        'total_quantity': total_quantity,
    }
    return render(request, 'products/index.html', context)

def products(request, category_id=None, page=1):
    if category_id:
        products = Product.objects.filter(category__id=category_id)
        total_items = len(Product.objects.filter(category__id=category_id))
    else:
        products = Product.objects.all()
        total_items = len(Product.objects.all())

    baskets = Basket.objects.filter(user=request.user)
    total_quantity = sum(basket.quantity for basket in baskets)
    total_sum = sum(basket.sum() for basket in baskets)
    paginator = Paginator(products, 3)
    products_paginator = paginator.page(page)
    context = {
        'title': 'Автосклад - каталог',
        'categories': ProductCategory.objects.all(),
        'products': products_paginator,
        'brands': Brand.objects.all(),
        'total_sum': total_sum,
        'total_quantity': total_quantity,
        'total_items': total_items,
    }

    return render(request, 'products/products.html', context)

# def products_fil(request, category_id):
#     baskets = Basket.objects.filter(user=request.user)
#     total_quantity = sum(basket.quantity for basket in baskets)
#     total_sum = sum(basket.sum() for basket in baskets)
#     context = {
#         'title': 'Автосклад - каталог',
#         'categories': ProductCategory.objects.all(),
#         'products': Product.objects.filter(category__id=category_id),
#         'brands': Brand.objects.all(),
#         'total_sum': total_sum,
#         'total_quantity': total_quantity,
#         'total_items': len(Product.objects.filter(category__id=category_id)),
#     }
#
#     return render(request, 'products/products.html', context)

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    baskets = Basket.objects.filter(user=request.user)
    total_quantity = sum(basket.quantity for basket in baskets)
    total_sum = sum(basket.sum() for basket in baskets)
    context = {
        'title': 'Автосклад - товар',
        'product': product,
        'categories': ProductCategory.objects.all(),
        'total_sum': total_sum,
        'total_quantity': total_quantity,
        'brands': Brand.objects.all(),
    }
    return render(request, 'products/product.html', context)

@login_required
def basket_add(request, product_id):
    current_page = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(current_page)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(current_page)

@login_required
def basket_delete(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def basket_item_inc(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    basket = baskets.first()
    basket.quantity += 1
    basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def basket_item_dec(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    basket = baskets.first()
    basket.quantity -= 1
    basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def search_res(request):
    query = request.GET.get('search_string')
    products = Product.objects.filter(name__iregex=query) | Product.objects.filter(description__iregex=query)

    baskets = Basket.objects.filter(user=request.user)
    total_quantity = sum(basket.quantity for basket in baskets)
    total_sum = sum(basket.sum() for basket in baskets)

    context = {
        'title': 'Автосклад - каталог',
        'categories': ProductCategory.objects.all(),
        'products': products,
        'brands': Brand.objects.all(),
        'total_sum': total_sum,
        'total_quantity': total_quantity,
        'total_items': len(products),
    }
    return render(request, 'products/products.html', context)

def order_add(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    orders = Order.objects.filter(user=request.user, basket=basket)
    order = orders.first()
    order.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def order_delete(request, id):
    order = Order.objects.get(id=id)
    order.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def contact(request):
    baskets = Basket.objects.filter(user=request.user)
    total_quantity = sum(basket.quantity for basket in baskets)
    total_sum = sum(basket.sum() for basket in baskets)
    context = {
        'title': 'Автосклад - контакты',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
        'brands': Brand.objects.all(),
        'total_sum': total_sum,
        'total_quantity': total_quantity,
    }
    return render(request, 'products/contact.html', context)



