"""Swiggy URL Configuration

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

from restaurant import views

urlpatterns = [

    path('',views.showMain,name="restro"),
    path('register/',views.registerPage,name="register"),
    path('save_res/',views.save_res,name="save_res"),
    path('restro_login/',views.restro_login,name="restro_login"),
    path('restro_login_check/',views.restro_login_check,name="restro_login_check"),
    path('restro_home/',views.restro_home,name="restro_home"),

]
