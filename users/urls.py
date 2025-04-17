from django.urls import path
from users.views import register, login

app_name = 'urls'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', register, name='register')
]
