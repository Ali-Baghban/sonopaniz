from django.contrib import admin
from .models import *

class AboutAdmin(admin.ModelAdmin):
    empty_value_display = '-Empty-'

admin.site.register(AboutModel, AboutAdmin)

class ExampleAdmin(admin.ModelAdmin):
    pass
admin.site.register(ExampleModel,ExampleAdmin)