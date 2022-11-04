from django.contrib import admin
from django.urls import path

from musicapp import views

urlpatterns = [
    path("", views.index, name='index'),
    path('hello/', views.hello),
]
