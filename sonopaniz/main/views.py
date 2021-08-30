from django.forms import forms
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView
from .forms import LoginForm, RegisterForm
from django.conf import settings
import requests


class MainView(View):
    def get(self,request):
        form_login = LoginForm
        form_register = RegisterForm
        
        context = { 'form_login':form_login, 'form_register': form_register, 'recaptcha_site_key':settings.GOOGLE_RECAPTCHA_SITE_KEY }
        return render(self.request, "main/index.html", context=context)
    
        
