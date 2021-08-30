from django.db import models

class ExampleModel(models.Model):
    caption = models.CharField(max_length=150,blank=True)
    photo   = models.ImageField(upload_to='application/%Y/%m/%d/')


class AboutModel(models.Model):
    name        = models.CharField(max_length=35,blank=False,default="Ali Baghban")
    description = models.TextField()
    photo       = models.ImageField(upload_to='profile/%Y/%m/%d/',blank=False)
    phone       = models.CharField(max_length=20,default="+989100366857")
    instagram   = models.CharField(max_length=20,default="alibaghban.ir")
    telegram    = models.CharField(max_length=20,default="alibaghban_ir")
    whatsapp    = models.CharField(max_length=20,default="+989100366857")
    other       = models.CharField(max_length=20,default="alibaghban.ir")

