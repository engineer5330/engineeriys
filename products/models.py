from django.db import models

from users.models import User


class BasketQueary(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)
    
    def total_sum_sale(self):
        return sum(basket.sum_with_sale() for basket in self)
    
    
    def sale_sum(self):
        return sum(basket.product.sale for basket in self)
    
    
    def total_sale_price(self):
        return sum(basket.product.total_sale() for basket in self)


class ProductCategory(models.Model):
    name =  models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = "жанр"
        verbose_name_plural = "жанры"
    
    def __str__(self):
        return f"{self.name}"


class Platform(models.Model):
    name =  models.CharField(max_length=128, unique=True)
    
    class Meta:
        verbose_name = "платформа"
        verbose_name_plural = "платформы"
    
    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quanity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    platform = models.ForeignKey(to=Platform, on_delete=models.CASCADE)
    sale = models.PositiveIntegerField(default=0)
    
    
    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"
    
    
    def total_price(self):
        return round(int(self.price) * (1 - self.sale / 100), 2)
    
    
    def total_sale(self):
        return round(int(self.price) * self.sale / 100, 2)
    
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
    
    
    def sum_with_sale(self):
        return self.product.total_price() * self.quantity


    


# class Order(models.Model):
#     user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    