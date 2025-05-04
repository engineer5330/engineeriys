from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator
from random import sample, choice

from products.models import ProductCategory, Product, Basket
from users.models import User


context = {
        'title': 'Engineeriys Store',
        
}


def index(request):
    if request.user.is_authenticated:
        context['basketsCount'] = Basket.objects.filter(user=request.user).count()
        
    products = sample(list(Product.objects.all()), 3)
    
    context['products'] = products
    context['page'] = 'index'
    
    


    return render(request, 'products/index.html', context)

def products(request, category_id=None, page_number = 1): 
    if request.user.is_authenticated:
        context['basketsCount'] = Basket.objects.filter(user=request.user).count()
        baskets = Basket.objects.filter(user=request.user)
        baskets_products = list(basket.product for basket in baskets)
    else:
        baskets = []
    
    baskets_products = list(basket.product for basket in baskets) 
    if category_id:
        category = ProductCategory.objects.get(id=category_id)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    per_page = 3
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)
    
    
    
    
    context['baskets_products'] = baskets_products
    context['products'] = products_paginator
    context['products_set'] = set(products_paginator)
    context['categories'] = ProductCategory.objects.all()
    context['count'] = Product.objects.all().count()
    context['page'] = 'catalog'
    
    return render(request, 'products/catalog.html', context)

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.filter(user=request.user, product=product)
    
    if not basket.exists():
        Basket.objects.create(user=request.user, product=product, quantity = 1)
    else:
        basket = basket.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_del(request, basket_id):
    basket = Basket.objects.filter(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def about(request):
    if request.user.is_authenticated:
        context['basketsCount'] = Basket.objects.filter(user=request.user).count()
    context['page'] = 'about'
    return render(request,'products/about.html', context)