from django.db import models
from servicecatalog.models import ServiceCatalog


class ServiceRequest(models.Model):
  id = models.BigAutoField(
    primary_key=True
  )
  
  text = models.TextField(
    max_length=1000,
    null=False,
    blank=False
  )

  creation_date = models.DateTimeField(
    auto_now_add=True,
    null=False,
    blank=False
  )

  last_updated = models.DateTimeField(
    auto_now=True,
    null=False,
    blank=False
  )

  name = models.CharField(
   max_length=50,
    null=False,
    blank=False
  )

  last_name =models.CharField(
     max_length=50,
    null=False,
    blank=False
  )
  mobile_no = models.TextField(
    max_length=20,
    null=False,
    blank=False,
    default=" "
  )
  #one to many relation to serviceCatalog
  service_id = models.ForeignKey(ServiceCatalog, on_delete=models.CASCADE,
    null=True,
    blank=False
    
  )

  class Meta:
    db_table = 'service_request'
