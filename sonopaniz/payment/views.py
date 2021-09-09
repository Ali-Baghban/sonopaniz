from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from cpanel.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from decouple import config
from idpay.api import IDPayAPI
from django.conf import settings
import uuid,json
import requests

def test(request):
    headers = {
    'Content-Type': 'application/json',
    'X-API-KEY': '6a7f99eb-7c20-4412-a972-6dfb7cd253a4',
    'X-SANDBOX': '1',
    }

    data = '{ "order_id": 101, "amount": 10000, "name": "Ali", "phone": "09382198592", "mail": "my@site.com", "desc": "xxxx", "callback": "http://127.0.0.1:8000/payment/test_callback" }'

    response = requests.post('https://api.idpay.ir/v1.1/payment', headers=headers, data=data,)
    response.encoding = 'utf-8'
    response = response.json()
    return redirect(response['link'])
@csrf_exempt
def test_callback(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        order_id = request.POST.get('order_id')
    headers = {
        'Content-Type': 'application/json',
        'X-API-KEY': '6a7f99eb-7c20-4412-a972-6dfb7cd253a4',
        'X-SANDBOX': '1',
    }
    data = {"id": id, "order_id":order_id}
    data = json.dumps(data)
    print(data)
    response = requests.post('https://api.idpay.ir/v1.1/payment/verify', headers=headers, data=data)
    response.encoding = 'utf-8'
    
    return HttpResponse(response)


def payment_start(request):
    if not request.user.is_authenticated :
        messages.error(request, "برای ارسال درخواست ابتدا وارد حساب کاربری خود شوید")
        return redirect('index')
    if request.method == 'POST':
        url = 'https://api.idpay.ir/v1.1/payment'
        headers = {
                    'Content-Type': 'application/json',
                    'X-API-KEY': settings.X_API_KEY,
                    'X-SANDBOX': '1',
                    }
        #headers = json.dumps(headers)
        order_id = str(uuid.uuid1())
        cat_name = request.POST['request_cat']
        cat_obj  = get_object_or_404(AdminList,title=cat_name)
        amount   = cat_obj.price  
        data = {
            'order_id' : order_id,
            'amount':amount,
            "callback": "http://127.0.0.1:8000/payment/callback",
            'mail': request.user.username,
        }
        data = json.dumps(data)
        record = Payment.objects.create(order_id=order_id, amount=int(amount))
        record.save()
        # response 
        response            = requests.post(url , headers=headers , data=data)
        response.encoding   = 'utf-8'
        response = response.json()
        
        # student request
        username    = get_object_or_404(User, username=request.user)
        #cat_name    = request.POST['request_cat']
        #cat_obj         = get_object_or_404(AdminList,title=cat_name)
        description = request.POST['request_description']
        if 'request_file' in request:
            request_file= request.FILES['request_file']
            obj         = StudentRequest.objects.create(username=username, title=cat_obj, description=description,request_file=request_file,order_id=order_id)
            obj.save()
            if 'id' in response:
                record.status = 1
                record.payment_id = response['id']
                record.save()
                #messages.success(request, "درخواست شما با موفقیت ثبت شد")
                return redirect(response['link'])
            else:
                messages.error(request, "در ثبت درخواست شما مشکلی به وجود آمده لطفا مجدد امتحان کنید")
                return redirect('cpanel')
                
        obj         = StudentRequest.objects.create(username=username, title=cat_obj, description=description,order_id=order_id)
        obj.save()
        
        if 'id' in response:
                record.status = 1
                record.payment_id = response['id']
                record.save()
                #messages.success(request, "درخواست شما با موفقیت ثبت شد")
                return redirect(response['link'])
        else:
            messages.error(request, "در ثبت درخواست شما مشکلی به وجود آمده لطفا مجدد امتحان کنید")
            return redirect('cpanel')     
    else:
        return redirect('cpanel')
        

@csrf_exempt
def payment_callback(request):
    if request.method == 'POST':
        
        pid = request.POST.get('id')
        status = request.POST.get('status')
        pidtrack = request.POST.get('track_id')
        order_id = request.POST.get('order_id')
        amount = request.POST.get('amount')
        card = request.POST.get('card_no')
        date = request.POST.get('date')

        if Payment.objects.filter(order_id=order_id, payment_id=pid, amount=amount, status=1).count() == 1:

            
            payment = Payment.objects.get(payment_id=pid, amount=amount)
            payment.status = status
            payment.date = str(date)
            payment.card_number = card
            payment.idpay_track_id = pidtrack
            payment.save()

            if str(status) == '10':
                url = 'https://api.idpay.ir/v1.1/payment/verify'
                headers = {
                'Content-Type': 'application/json',
                'X-API-KEY': settings.X_API_KEY,
                'X-SANDBOX': '1',
                }
                #headers = json.dumps(headers) 
                data = {"id": pid, "order_id":order_id}
                data = json.dumps(data)
                response = requests.post(url , headers=headers, data=data)
                response.encoding = 'utf-8'
                response = response.json()
                print(response)
                if 'status' in response:

                    payment.status = response['status']
                    payment.bank_track_id = response['payment']['track_id']
                    payment.save()
                    obj         = StudentRequest.objects.get(order_id=order_id)
                    obj.is_payed=True
                    obj.save()
                    messages.success(request, "درخواست شما با موفقیت ثبت شد")
                    return redirect('cpanel')

                else:
                    txt = response['message']
                    messages.error(request, txt)
            else:
                txt = "Error Code : " + str(status) 
                messages.error(request, txt)
        else:
            txt = "Order Not Found"
            messages.error(request, txt)

    else:
        txt = "Bad Request"
        messages.error(request, txt)

    return redirect('cpanel')

        

