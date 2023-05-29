import django_filters
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.forms import model_to_dict, modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
import datetime
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

from .forms import PostForm1, PostForm2, PostForm3
from .models import *

from users.models import Profile


class PostListView(ListView, LoginRequiredMixin):
    model = Post
    template_name = 'main/main.html'
    context_object_name = 'posts'

    def get_queryset(self):
        profile_list = Profile.objects.filter(address=self.request.user.profile.address)  # Получили список нужных нам
        # профилей

        queryset = Post.objects.filter(author__profile__in=profile_list).order_by('-date_posted')  # Получ нужные posts

        if self.request.GET.get("date"):
            date = self.request.GET.get("date")
        else:
            date = (datetime.datetime.now() + datetime.timedelta(days=0)).date()

        queryset = queryset.filter(date_deliver=date)  # Достаем все посты с данной датой

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile_list = Profile.objects.filter(address=self.request.user.profile.address)  # Получили список нужных нам
        # профилей

        queryset = Post.objects.filter(author__profile__in=profile_list).order_by('-date_posted')  # Получ нужные posts

        date = (datetime.datetime.now() + datetime.timedelta(days=0)).date()
        cnt_posts1 = queryset.filter(date_deliver=date).count()

        date = (datetime.datetime.now() + datetime.timedelta(days=1)).date()
        cnt_posts2 = queryset.filter(date_deliver=date).count()

        date = (datetime.datetime.now() + datetime.timedelta(days=2)).date()
        cnt_posts3 = queryset.filter(date_deliver=date).count()

        date = (datetime.datetime.now() + datetime.timedelta(days=3)).date()
        cnt_posts4 = queryset.filter(date_deliver=date).count()

        date = (datetime.datetime.now() + datetime.timedelta(days=4)).date()
        cnt_posts5 = queryset.filter(date_deliver=date).count()

        date = (datetime.datetime.now() + datetime.timedelta(days=5)).date()
        cnt_posts6 = queryset.filter(date_deliver=date).count()

        date = (datetime.datetime.now() + datetime.timedelta(days=6)).date()
        cnt_posts7 = queryset.filter(date_deliver=date).count()

        context['cnt_posts1'] = cnt_posts1
        context['cnt_posts2'] = cnt_posts2
        context['cnt_posts3'] = cnt_posts3
        context['cnt_posts4'] = cnt_posts4
        context['cnt_posts5'] = cnt_posts5
        context['cnt_posts6'] = cnt_posts6
        context['cnt_posts7'] = cnt_posts7

        return context


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


class PostCreateView1(LoginRequiredMixin, CreateView, FormView):
    form_class = PostForm1
    template_name = 'main/post_form1.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostCreateView2(LoginRequiredMixin, CreateView, FormView):
    form_class = PostForm2
    template_name = 'main/post_form2.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostCreateView3(LoginRequiredMixin, CreateView, FormView):
    form_class = PostForm3
    template_name = 'main/post_form3.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm1
    template_name = 'main/post_form1.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostUpdateView2(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm2
    template_name = 'main/post_form2.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostUpdateView3(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm3
    template_name = 'main/post_form3.html'
    success_url = '/'

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
#     return render(request, 'main/post_form1.html', data)




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
#     return render(request, 'main/post_form1.html', data)
