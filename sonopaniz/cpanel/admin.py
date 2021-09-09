from django.contrib import admin
from .models import *

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email',]
    list_per_page = 20
admin.site.register(Comment, CommentAdmin)

class AdminfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'description','is_published']
    list_editable = ['is_published']
    list_per_page = 5
admin.site.register(AdminFile,AdminfileAdmin)

class AdminListAdmin(admin.ModelAdmin):
    list_display = ['title', 'price','is_published']
    list_editable = ['is_published']
    list_per_page = 5
admin.site.register(AdminList,AdminListAdmin)

class StudentRequestAdmin(admin.ModelAdmin):
    list_display = ['username', 'title','is_payed','is_done']
    list_display_links = ['username','title']
    list_filter = ['is_payed', 'is_done']
    search_fields = ['username', 'title']
    list_editable = ['is_done']
    list_per_page = 25
admin.site.register(StudentRequest,StudentRequestAdmin)

class AdminLearningAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published']
    list_editable= ['is_published']
    list_per_page= 5

admin.site.register(AdminLearning,AdminLearningAdmin)