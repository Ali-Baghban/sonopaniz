
from django import forms
from django.forms.formsets import formset_factory
from django.forms.widgets import PasswordInput

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.EmailInput,required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    username.widget.attrs.update({'id':'username','class':'form-control', 'style': 'text-align: center;','placeholder':'نام کاربری'})
    password.widget.attrs.update({'id':'password','class':'form-control','style': 'text-align: center;','placeholder':'پسورد'})

class RegisterForm(forms.Form):
    name    = forms.CharField(required=True)
    password= forms.CharField(widget=PasswordInput,required=True)
    re_pass = forms.CharField(widget=PasswordInput,required=True)
    email   = forms.CharField(widget=forms.EmailInput, required=True)

    name.widget.attrs.update({'id':'password','class':'form-control','style': 'text-align: center;','placeholder':'نام شما'})
    password.widget.attrs.update({'id':'password','class':'form-control','style': 'text-align: center;','placeholder':'پسورد'})
    re_pass.widget.attrs.update({'id':'password','class':'form-control','style': 'text-align: center;','placeholder':'تکرار پسورد'})
    email.widget.attrs.update({'id':'password','class':'form-control','style': 'text-align: center;','placeholder':'ایمیل شما'})
