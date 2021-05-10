from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # logg in page
    path('create_user', views.create_user),
    #renders to logIn Page
    path('loginPage', views.login_page),
    # login users
    path('login', views.login),
    # logout user
    path('logout', views.logout),
]
