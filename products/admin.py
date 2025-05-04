from django.contrib import admin
from products.models import Product, ProductCategory, Basket, Platform

admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'platform','quanity', 'category')
    fields = ('name', 'description', ('price', 'sale'), 'quanity', 'image','category', 'platform')
    search_fields = ['name']
    ordering = ['name']
    
    

class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ['product', 'quantity', 'created_on_time']
    readonly_fields = ['created_on_time']
    extra = 0

    
@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    model = Platform
    fields = ['name']