from django.contrib import admin
from .models import ServiceRequest
from servicecatalog.models import ServiceCatalog
# Register your models here.
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ['name','last_name','mobile_no','creation_date','service']
    search_fields = ['service_id','name','last_name','mobile_no']
    readonly_fields = ('service',)

    def service(self,o):
        return o.name
    

 
admin.site.register(ServiceRequest,ServiceRequestAdmin)

