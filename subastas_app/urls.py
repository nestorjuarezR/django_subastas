from django.contrib import admin
from django.urls import path, include  # modificada
from . import views

urlpatterns = [
   path("", views.index, name="index"),
]