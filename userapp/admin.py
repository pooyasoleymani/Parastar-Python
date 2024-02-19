from django.contrib import admin
from todolist.models import Todo
from todolist.serviceRequest2 import ServiceRequest

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ['text','creation_date','last_updated','id']

class ServiceRequestAdmin(admin.ModelAdmin):
    list_display=['name','last_name','creation_date','last_updated','text']
    
        
    
admin.site.register(ServiceRequest,ServiceRequestAdmin)    
admin.site.register(Todo,TodoAdmin)
