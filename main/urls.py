from django.urls import path, include
from . import views
from django.contrib import admin
# from main.views import register


urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),


    # path('filter/<int:pk>', services.order_filter, name='order_filter'),
]
