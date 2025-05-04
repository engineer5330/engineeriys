from django.urls import path
from users.views import register, login, profile, logout

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('edit/', profile, name='editprofile'),
    path('basket/', profile, name='basket'),
    path('logout/', logout, name='logout'),

]
