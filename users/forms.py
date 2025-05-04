from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from django.contrib.auth import get_user_model
User = get_user_model()

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4", 'placeholder': 'Введите имя пользователся'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control py-4", 'placeholder': 'Введите пароль'
    }))
    
    
    class Meta():
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control", 'placeholder': 'Введите имя'
    }))
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control", 'placeholder': 'Введите фамилию'
    }))
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control", 'placeholder': 'Введите логин' 
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': "form-control", 'placeholder': 'Введите электронную почту'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control", 'placeholder': 'Введите пароль'
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control", 'placeholder': 'Повторите пароль'
    }))
    
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control", 'placeholder': 'Введите номер телефона' 
    }))
    
    
class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')
    
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4"
    }))
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4"
    }))
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4", 'readonly': False
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': "form-control py-4", 'readonly': True
    }))
    
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': "custom-file-input"}), required = False)