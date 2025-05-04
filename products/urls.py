from django.urls import path
from products.views import products, basket_add, basket_del, about

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('page/<int:page_number>/', products, name='paginator'),
    path('category/<int:category_id>', products, name='category'),
    path('baskets/add/<int:product_id>', basket_add, name='basket_add'),
    path('baskets/del/<int:basket_id>', basket_del, name='basket_del'),
    
]
