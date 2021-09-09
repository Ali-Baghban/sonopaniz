from os import stat
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404,get_list_or_404
from .forms import CommentForm, LoginForm, RegisterForm
from django.conf import settings
import requests
from .models import *


def index(request):
    status      = get_object_or_404(Setting, option="Site Status").status
    if  not status:
        return redirect('downpage')

    form_login      = LoginForm
    form_register   = RegisterForm
    template_name   = "main/index.html"
    about       = About.objects.get(pk=1)
    apps        = Example.objects.filter(is_published=True)
    context     = {'form_login' : form_login, 'form_register': form_register,
    'about': about, 'apps': apps, 'status' : status}
    return render(request, template_name, context=context)

def downpage(request):
    return render(request, "main/down.html")