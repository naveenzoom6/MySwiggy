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
from s_admin import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.admin_login,name='admin_login'),
    path('admin_login_check/',views.admin_login_check,name="admin_login_check"),
    path('admin_home/',views.admin_home,name="admin_home"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),

    #state
    path('open_state/',views.open_state,name="open_state"),
    path('save_state/',views.save_state,name="save_state"),
    path('update_state/',views.update_state,name="update_state"),
    path('update_state_data/',views.update_state_data,name="update_state_data"),
    path('delete_state/',views.delete_state,name='delete_state'),

    #City
    path('open_city/', views.open_city, name="open_city"),
    path('save_city/', views.save_city, name="save_city"),
    # path('update_city/', views.update_city, name="update_city"),
    # path('update_city_data/', views.update_city_data, name="update_city_data"),
    # path('delete_city/', views.delete_city, name='delete_city'),

    #Area
    path('open_area/', views.open_area, name="open_area"),
    path('save_area/', views.save_area, name="save_area"),
    # path('update_area/', views.update_area, name="update_area"),
    # path('update_area_data/', views.update_area_data, name="update_area_data"),
    # path('delete_area/', views.delete_area, name='delete_area'),

]
