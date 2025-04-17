from django.shortcuts import render, HttpResponse

from products.models import ProductCategory, Product
def index(request):
    context = {
        'title': 'Store'
    }
    return render(request, 'index.html', context)


def products(request):
    context = {
        'title':'Catalog',
        'items':  Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }
        
    return render(request, 'products.html', context)
