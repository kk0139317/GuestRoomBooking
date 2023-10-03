from django.urls import path
from django.urls import include, path
from. import  views
from django.shortcuts import get_object_or_404, render
from owner import views as ownerview

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('service', views.service, name="service"),
    path('room', views.rooms, name="rooms"),
    path('booking/', views.booking, name="booking"),
    path('contact', views.contact, name="contact"),
    path('create-user', views.CreateUser, name="CreateUser"),
    path('login', views.loginuser, name="LoginUser"),
    path('booking/<int:pid>/', views.booking, name="booking"),
    path('logoutuser', ownerview.CustomLogout, name='logout'),
    path('profile', views.profile, name='Profile'),
    # path('auth', views.Auth_Log, name="Authntification"),
    # path('create-user', views.CreateUser, name="CreateUser"),
    # path('login', views.loginuser, name="LoginUser"),
]
