from django.contrib.auth.decorators import login_required
from django.forms import model_to_dict, modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.template import RequestContext
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout
from django.views.generic.edit import CreateView, FormView
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
# from .forms import ImageForm

from .models import *


# def image_upload_view(request):
#     """Process images uploaded by users/обработчик формы"""
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # Get the current instance object to display in the template
#             img_obj = form.instance
#             return render(request, 'main/create_form.html', {'form': form, 'img_obj': img_obj})
#     else:
#         form = ImageForm()
#     return render(request, 'main/create_form.html', {'form': form})


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'main/main.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'main/main.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class UserPostListView(ListView):
    model = Post
    template_name = 'main/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'price', 'price_deliver', 'cnt_people', 'date_deliver', 'time_deliver', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'price', 'price_deliver', 'cnt_people', 'date_deliver', 'time_deliver', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False











# def create(request):
#     if request.method == 'POST':
#         error = ''
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('main')
#         else:
#             error = 'Форма некорректна'
#
#     form = PostForm()
#     data = {
#         'form' : form,
#         'error' : error
#     }
#
#     return render(request, 'main/post_form.html', data)




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
#     return render(request, 'main/post_form.html', data)
