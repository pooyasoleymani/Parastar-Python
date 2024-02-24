from django.contrib import admin
from .models import ServiceCatalog
# Register your models here.
class ServiceCatalogAdmin(admin.ModelAdmin):
    list_display = ['name','creation_date']
    search_fields = ['name']
    list_filter = ['id']

admin.site.register(ServiceCatalog,ServiceCatalogAdmin)