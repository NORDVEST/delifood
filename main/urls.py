from django.urls import path, include
from . import views
from django.contrib import admin
from .views import (
    PostListView,
    PostListCreate,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
# from main.views import register


urlpatterns = [
    path('create/', views.create, name='create'),
    path('', PostListView.as_view(), name='home'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/create', PostListCreate.as_view(), name='blog-create')


    # path('filter/<int:pk>', services.order_filter, name='order_filter'),
]
