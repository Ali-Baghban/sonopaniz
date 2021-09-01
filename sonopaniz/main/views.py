
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from .forms import LoginForm, RegisterForm
from django.conf import settings
import requests
from .models import *


class MainView(View):
    def get(self,request):
        form_login      = LoginForm
        form_register   = RegisterForm
        about           = get_object_or_404(AboutModel, pk=1)
        context = { 'form_login':form_login, 'form_register': form_register,
         'about': about, 'recaptcha_site_key':settings.GOOGLE_RECAPTCHA_SITE_KEY }
        return render(self.request, "main/index.html", context=context)
    
        
