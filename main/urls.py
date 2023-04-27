from django.urls import path, include
from . import views
from django.contrib import admin
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
# from main.views import register


urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.create, name='blog-about')


    # path('filter/<int:pk>', services.order_filter, name='order_filter'),
]
