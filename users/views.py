from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from users.forms import UserRegistrationForm, UserLoginForm, UserProfileForm
from products.models import Basket

context = {
    'title': 'Engineeriys-Store',
    'navbar': 'Engineeriys Store'
}



@login_required
def profile(request):
    if request.user.is_authenticated:
        context['basketsCount'] = Basket.objects.filter(user=request.user).count()
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))      
    elif request.path == "/users/edit/":
        form = UserProfileForm(instance=request.user)
        context["form"] = form
        context['page'] = 'edit'
        return render(request, 'users/edit.html', context)
    elif request.path == "/users/basket/":
        context['baskets'] = Basket.objects.filter(user=request.user)
        context['page'] = 'basket'
        return render(request, 'users/basket.html', context)
    elif request.path == "/users/profile/":
        context['page'] = 'profile'
        return render(request, 'users/profile.html', context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))          
                
    else:
        form = UserLoginForm()
    context = {
        'title': 'Engineeriys-Store',
        'navbar': 'Engineeriys Store',
        'form': form}
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('users:login'))      

    else:
        form = UserRegistrationForm()
    context = {
        'title': 'Engineeriys-Store',
        'navbar': 'Engineeriys Store',
        'form': form}     
    return render(request, 'users/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


