from os import name
from django.db.models.base import Model
from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name="index"),
    path('down', downpage, name='downpage'),
]