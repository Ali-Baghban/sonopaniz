from django.contrib import admin
from .models import *

class AboutAdmin(admin.ModelAdmin):
    empty_value_display = '-Empty-'

admin.site.register(About, AboutAdmin)

class ExampleAdmin(admin.ModelAdmin):
    pass
admin.site.register(Example,ExampleAdmin)

class SettingAdmin(admin.ModelAdmin):
    pass
admin.site.register(Setting, SettingAdmin)