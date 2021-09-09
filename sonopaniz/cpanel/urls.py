from os import name
from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='cpanel'),
    path('rq', request_send, name='request_send'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('register', register, name='register'),
    path('comment', comment , name='comment'),
    path('dl/<str:filepath>', download, name='download'),
]