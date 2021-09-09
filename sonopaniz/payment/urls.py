from django.urls import path
from .views import *
urlpatterns = [
    path('', payment_start, name='payment_start'),
    path('callback', payment_callback, name='callback'),
    path('test', test , name='test'),
    path('test_callback', test_callback, name='test_callback'),
]