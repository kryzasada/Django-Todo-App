"""TO_DO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from login.views import user_register, user_login_in

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', user_register,  name='register'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'),  name='login'),
    path('register/login',
         auth_views.LoginView.as_view(template_name='login.html', extra_context={'register': 1}), name='register-login'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'),  name='logout'),
    path('login1', user_login_in,  name='zalogowany'),
    path('', auth_views.LoginView.as_view(template_name='login.html'),  name='start'),
]
