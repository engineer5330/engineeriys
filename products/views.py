from django.shortcuts import render, HttpResponse

def index(request):
    context = {
        'title': 'Store'
    }
    return render(request, 'index.html', context)


def products(request):
    context = {
        'title':'Catalog',
        'items':  [
            {
            "image":"/static/vendor/img/products/Adidas-hoodie.png",
            "name":"Худи черного цвета с монограммами adidas Originals",
            "price":6090,
            "text":"Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни."
            },
            {
            "image":"/static/vendor/img/products/Blue-jacket-The-North-Face.png",
            "name":"Синяя куртка The North Face",
            "price":23725,
            "text":"Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель."
            }
            
            
        ]
    }
        
    return render(request, 'products.html', context)
