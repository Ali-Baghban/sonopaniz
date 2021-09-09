from django.shortcuts import get_object_or_404, redirect, render
from django.http import FileResponse
import requests
from .models import *
from main.forms import *
from django.contrib import auth, messages


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "لطفا وارد حساب کاربری تان شوید")
        return redirect('index')
    template_name       = "cpanel/index.html"
    file_general        = AdminFile.objects.all().filter(is_published=True)
    admin_list          = AdminList.objects.all().filter(is_published=True)
    user                = request.user
    student_requests    = StudentRequest.objects.all().filter(username=user)
    admin_learning      = AdminLearning.objects.all().filter(is_published=True)
    context             = {
         'file_general' : file_general, 'admin_list':admin_list, 'student_requests':student_requests,
        'admin_learning':admin_learning,
                            }
    return render(request, template_name, context=context)

def request_send(request):
    if not request.user.is_authenticated :
        messages.error(request, "برای ارسال درخواست ابتدا وارد حساب کاربری خود شوید")
        return redirect('index')
    if request.method == "POST":
        username    = get_object_or_404(User, username=request.user)
        cat_name    = request.POST['request_cat']
        cat_obj         = get_object_or_404(AdminList,title=cat_name)
        description = request.POST['request_description']+str(cat_obj.price)
        if 'request_file' in request:
            request_file= request.FILES['request_file']
            obj         = StudentRequest.objects.create(username=username, title=cat_obj, description=description,request_file=request_file)
            obj.save()
            messages.success(request, "درخواست شما با موفقیت ثبت شد")
            return redirect('cpanel')
        obj         = StudentRequest.objects.create(username=username, title=cat_obj, description=description)
        obj.save()
        messages.success(request, "درخواست شما با موفقیت ثبت شد")
        return redirect('cpanel')
    else:
        return redirect('cpanel')
def login(request):
    if request.method == "POST":
        username        = request.POST['username']
        password        = request.POST['password']
        user            = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "خوش آمدید")
            return redirect('cpanel')
        else:
            messages.error(request, "پسورد یا نام کاربری اشتباه است")
            return redirect('index')
    else:
        return redirect('index')

def logout(request):
    auth.logout(request)
    messages.success(request, "با موفقیت از حسابتان خارج شدید")
    return redirect('index')

def register(request):
    if request.method == "POST":
        email           = request.POST['email']
        name            = request.POST['name']
        password        = request.POST['password']
        re_pass         = request.POST['re_pass']
        if password != re_pass : 
            messages.error(request, "پسورد های وارد شده مشابه نمی باشند")
            return redirect('index')
        user            = User.objects.filter(username=email)
        if user.exists():
            messages.error(request, "این نام کاربری در سیستم وجود دارد")
            return redirect('index')
        user            = User.objects.create_user(username=email , password=password)
        user.email      = email
        user.first_name = name
        user.save()
        auth.login(request, user)
        messages.success(request, "خوش آمدید")
        return redirect('cpanel')     
    else:
        messages.error(request, "FUCK you fuckable hacker !")
        return redirect('index')

def comment(request):
    if request.method == "POST":
        email           = request.POST['email']
        name            = request.POST['name']
        message         = request.POST['message']
        if not message:
            messages.error(request, "انتقاد یا پیام شما فاقد متن است")
            return redirect('index')
        comment         = Comment.objects.create(name=name, email=email, message=message)
        messages.success(request, "پیام شما با موفقیت ارسال شد")
        return redirect('index')

def download(request,filepath):
    #obj        = get_object_or_404(StudentRequest, id=id)
    #filename   = obj.response_file.path
    if 'media' in filepath:
        filename   = filepath
        response   = FileResponse(open(filename,'rb'))
        return response
    messages.error(request, "فایلی با این نام وجود ندارد یا شما دسترسی لازم جهت دانلود را ندارید")
    return redirect('cpanel')