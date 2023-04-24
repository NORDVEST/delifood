from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import HttpResponse  # delete if no use
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.views.generic.edit import CreateView
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

# from .forms import OrdersForm
from .models import *


class MainView(TemplateView):
    template_name = 'main/index.html'

    #
class RegistrationView(FormView):



# class SignUp(CreateView, generic.ListView):
#     model = Adress
#     context_object_name = 'data_adress'  # ваше собственное имя переменной контекста в шаблоне
#     form_class = SignUpForm
#     success_url = reverse_lazy("login")  # Перебрасываем на страницу входа в случае успеха
#     queryset = Adress.objects.all()
#     template_name = "main/signup.html"
#
#
def index(request):
    # data = Orders.objects.all()

    return render(request, 'main/index.html')


def friends(request):
    return HttpResponse("<h4>Страница с друзьями</h4>")


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
