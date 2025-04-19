from django.shortcuts import render, HttpResponseRedirect
# from django.contrib import auth
from django.urls import reverse

from users.forms import UserRegistrationForm, UserLoginForm

# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
                
#     else:
#         form = UserLoginForm()
#     context = {'form': form}
#     return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        print(request.POST['username'])
        _data = {'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'],'username': request.POST['username'], }
        _form = UserRegistrationForm(data=request.POST)
        print(_form.is_valid())
        if _form.is_valid():
            _form.save()
            return HttpResponseRedirect(reverse('users  :login'))      
    else:
        _form = UserRegistrationForm()
        context = {'form': _form}     
        return render(request, 'users/register.html', context)