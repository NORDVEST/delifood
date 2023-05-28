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
    PostUpdateView2,
    PostUpdateView3,

    PostDeleteView
)
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(login_url='/login/')(PostListView.as_view()), name='home'),
    path('user/<str:username>', login_required(login_url='/login/')(UserPostListView.as_view()), name='user-posts'),
    path('post/<int:pk>/', login_required(login_url='/login/')(PostDetailView.as_view()), name='post-detail'),

    path('post/new/1', PostCreateView1.as_view(), name='post-create'),
    path('post/new/2', PostCreateView2.as_view(), name='post-create2'),
    path('post/new/3', PostCreateView3.as_view(), name='post-create3'),

    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/update/', PostUpdateView2.as_view(), name='post-update2'),
    path('post/<int:pk>/update/', PostUpdateView3.as_view(), name='post-update3'),

    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # path('upload/', views.image_upload_view)
]
