from os import name
from datetime import datetime
from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING
class Comment(models.Model):
    name        = models.CharField(max_length=40,blank=True,null=True)
    email       = models.EmailField(blank=True, null=True)
    message     = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class AdminFile(models.Model):
    name        = models.CharField(max_length=40, blank=False, unique=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    file        = models.FileField(upload_to='files/mine/%Y/%m/%d', null=True)
    is_published= models.BooleanField(null=True , default=True)

    def __str__(self):
        return self.name


class AdminList(models.Model):
    related_file= models.ForeignKey(AdminFile, on_delete=models.CASCADE)
    title       = models.CharField(max_length=35,  unique=True, null=True, blank=False)
    description = models.CharField(max_length=100, blank=True, null=True)
    price       = models.CharField(max_length=30, blank=False, null=True)
    is_published= models.BooleanField(null=True , default=True)
    def __str__(self):
        return self.title
class AdminLearning(models.Model):
    title       = models.CharField(max_length=35,  unique=True, blank=False)
    video_url   = models.CharField(max_length=350,  unique=True, default='#')
    is_published= models.BooleanField(null=True , default=True)
    def __str__(self):
        return self.title

class StudentRequest(models.Model):
    username        = models.ForeignKey(User, on_delete=models.CASCADE)
    title           = models.ForeignKey(AdminList, on_delete=DO_NOTHING ,null=True)
    request_file    = models.FileField(upload_to='files/customers/%Y/%m/%d', validators=[FileExtensionValidator(['pdf','docx','doc'])] ,blank=True, null=True)
    response_file   = models.FileField(upload_to='files/customers/%Y/%m/%d', validators=[FileExtensionValidator(['pdf','docx','doc'])] ,blank=True, null=True)
    description     = models.TextField(blank=True, null=True)
    order_id        = models.TextField(blank=True ,)
    is_payed        = models.BooleanField(default=False,)
    is_done         = models.BooleanField(default=False, null=True)
    date            = models.DateTimeField(default=datetime.now, blank=True, null=True)

    def __str__(self):
        return self.username.username 
