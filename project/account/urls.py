from django.urls import path
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', lambda request: redirect('login')),  # This redirects to /login/
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('server-register/', views.server_register, name='server_register'),
    path('client-register/', views.client_register, name='client_register'),
    path('home/', views.home, name='home'),
]
