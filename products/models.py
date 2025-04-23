from django.db import models

from users.models import User


class BasketQueary(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

class ProductCategory(models.Model):
    name =  models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
    
    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quanity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
    
    
    def __str__(self):  
        return f"{self.name}"


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_on_time = models.DateTimeField(auto_now_add = True)
    
    
    objects = BasketQueary.as_manager()
    
    def __str__(self):
        return f"Корзина для {self.user.username} Содержимое: {self.product}"
    
    
    def sum(self):
        return self.product.price * self.quantity