from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth import get_user_model
CustomUser = get_user_model()

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4", 'placeholder': 'Введите имя пользователся'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control py-4", 'placeholder': 'Введите пароль'
    }))
    
    
    class Meta:
        model = CustomUser
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    class Metha:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'password2')
        
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4", 'placeholder': 'Введите имя'
    }))
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4", 'placeholder': 'Введите фамилию'
    }))
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4", 'placeholder': 'Введите логин' 
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': "form-control py-4", 'placeholder': 'Введите электронную почту'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control py-4", 'placeholder': 'Введите пароль'
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control py-4", 'placeholder': 'Повторите пароль'
    }))
    
    
    