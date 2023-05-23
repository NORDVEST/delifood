from django.urls import path, include
from django.contrib import admin
from .views import (
    PostListView,
    UserPostListView,
    PostDetailView,

    PostCreateView1,
    PostCreateView2,
    PostCreateView3,

    PostUpdateView,
    PostDeleteView
)
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView1.as_view(), name='post-create'),
    path('post/new/2', PostCreateView2.as_view(), name='post-create2'),
    path('post/new/3', PostCreateView3.as_view(), name='post-create3'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # path('upload/', views.image_upload_view)

    # path('filter/<int:pk>', services.order_filter, name='order_filter'),
]
