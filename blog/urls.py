from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name=' st'),
]
from django.shortcuts import render # Create your views here.
