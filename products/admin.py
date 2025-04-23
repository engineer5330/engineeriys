from django.contrib import admin
from products.models import Product, ProductCategory, Basket

admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quanity', 'category')
    fields = ('name', 'description', ('price', 'quanity'), 'image','category')
    readonly_fields = ('description',)
    search_fields = ['name']
    ordering = ['name']
    

class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ['product', 'quantity', 'created_on_time']
    readonly_fields = ['created_on_time']
    extra = 0