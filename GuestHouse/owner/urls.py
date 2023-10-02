from django.urls import path
from django.urls import include, path
from. import  views


urlpatterns = [
    path('', views.index, name="index"),
    path('create-user', views.CreateUser, name="CreateUser"),
    path('login', views.loginuser, name="LoginUser"),
    path('room', views.room, name="Room "),
    path('add_room', views.add_room, name="add_room"),
    path('logoutuser', views.CustomLogout, name='logout'),
    path('profile', views.profile, name='adminprofile'),
    path('edit/<int:pid>', views.edit, name='edit_room'),
]
