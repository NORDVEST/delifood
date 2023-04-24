from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout
from django.views.generic.edit import CreateView, FormView
from django.views import generic
from django.views.generic import TemplateView


from .models import *


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'main/main.html', context)


def create(request):
    return render(request, 'main/create.html', {'title': 'О клубе Python Bytes'})


#  class SignUp(CreateView, generic.ListView):
#     model = Adress
#     context_object_name = 'data_adress'  # ваше собственное имя переменной контекста в шаблоне
#     form_class = SignUpForm
#     success_url = reverse_lazy("login")  # Перебрасываем на страницу входа в случае успеха
#     queryset = Adress.objects.all()
#     template_name = "main/signup.html"


# def register(request):
#
#     if request.POST == 'POST':
#         form = UserCreationForm(request.POST)  # заполняем его данными из поста
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Вы успешно зарегистрировались')
#             return redirect('login')  # теперь перебрасываем зарегистрированного на страницу авторизации
#         else:
#             messages.error(request, 'Ошибка регистрации')
#     else:
#         form = UserCreationForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'main/registration.html', context)
#
#
# def create(request):
#     error = ''
#     if request.method == 'POST':
#         form = OrdersForm(request.POST)
#         if form.is_valid():
#             form.save()
#         else:
#             error = 'Некорректно введены данные'
#     form = OrdersForm()
#     data = {
#         'form': form,
#         'error': error
#     }
#
#     return render(request, 'main/create.html', data)
