from django.contrib import admin
from django.urls import path, include
from .views import register
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'user/logout.html'), name='logout'),
]
