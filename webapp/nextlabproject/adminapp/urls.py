from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('signOn', views.signOn, name='signOn'),
    path('app/<str:username>',views.app,name='adminhome'),
    path('register',views.register,name='register'),
]