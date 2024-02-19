from django.db import models

# Create your models here.
class ServiceCatalog(models.Model):
  id = models.BigAutoField(
    primary_key=True
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

  class Meta:
    db_table = 'service_catalog'


