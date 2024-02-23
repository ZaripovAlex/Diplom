from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from .forms import RegForm, LoginUserForm
from .models import User
from recipe.models import Category, Recipe


def profile(request, user_id):
    user = User.objects.filter(pk=user_id).first()
    recipe = [get_object_or_404(Recipe, author=user)]
    context = {
        'title': f'Профиль полльзователя: {user.username}',
        'recipes': recipe,
        'user': user,
    }
    return render(request, 'profile.html', context)


# def user_registration(request):
#     form = None
#     if request.method == 'POST':
#         form = RegForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             firstname = form.cleaned_data['firstname']
#             lastname = form.cleaned_data['lastname']
#             email = form.cleaned_data['email']
#             image = form.cleaned_data['image']
#             user = User(
#                 username=username,
#                 firstname=firstname,
#                 lastname=lastname,
#                 email=email,
#                 image=image,)
#             user.save()
#         else:
#             form = RegForm()
#     context = {
#         'title': 'Регистрация пользователя!',
#         'form': form,
#     }
#     return render(request, 'registration.html',  context)


# @login_required
# def profile(request):
#     username = request.user.username
#     user = User.objects.get(username=username)
def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('Home'))
    else:
        form = LoginUserForm()
    return render(request, 'login.html', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('Home'))

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'login.html'




class CreateUser(CreateView):
    model = User
    form_class = RegForm
    template_name = 'registration.html'