from os import stat_result
from django.db import models
from django.db.models.fields.files import ImageField

class Setting(models.Model):
    CHOICES     = (
        ('Site Status','Site Status'),
    )
    option      = models.CharField(max_length=20, choices=CHOICES, unique=True)
    CHOICES     = (
        (True,'Site Up'),
        (False,'Site Down'),
    )
    status      = models.BooleanField(choices=CHOICES,null=True,default=True)

    def __str__(self):
        return self.option
class Example(models.Model):
    title       = models.CharField(max_length=50, blank=False,null=True)
    caption     = models.CharField(max_length=150,blank=False, null=True)
    photo       = models.ImageField(upload_to='application/%Y/%m/%d/', blank=False, null=True)
    is_published= models.BooleanField(default=False,null=True)
    def __str__(self):
        return self.title

class About(models.Model):
    name        = models.CharField(max_length=35,blank=False,default="Ali Baghban")
    description = models.TextField()
    photo       = models.ImageField(upload_to='profile/%Y/%m/%d/',blank=False)
    youtube     = models.CharField(max_length=20,default="#")
    instagram   = models.CharField(max_length=20,default="sonopaniz")
    telegram    = models.CharField(max_length=20,default="#")
    whatsapp    = models.CharField(max_length=20,default="#")
    other       = models.CharField(max_length=20,default="alibaghban.ir")
    def __str__(self):
        return self.name

