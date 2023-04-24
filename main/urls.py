from django.urls import path, include,re_path
from . import views
from django.contrib import admin
# from main.views import register


urlpatterns = [
    path('', views.index, name='home'),  # мы обращаемся к методу, если же прописывать метод с круглыми скобками,
    # то мы выполним его
    path('friends', views.friends, name='friends'),
    # path('signup', views.SignUp.as_view(), name="signup"),
    # path('create', views.create, name='create'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('filter/<int:pk>', services.order_filter, name='order_filter'),
    path('admin/', admin.site.urls)
]
