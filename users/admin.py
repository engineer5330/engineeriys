from django.contrib import admin

from users.models import User
from products.admin import BasketAdmin



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'date_joined', 'last_login']
    search_fields = ['username', 'email']
    readonly_fields = ['date_joined', 'last_login', 'is_superuser']
    inlines = [BasketAdmin]
    
    
