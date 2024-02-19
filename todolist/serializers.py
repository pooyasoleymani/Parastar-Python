from rest_framework import serializers
from .models import Todo ,ServiceRequest
from .mymodels.serviceCatalog import ServiceCatalog


class TodoSerializer(serializers.ModelSerializer):
  text = serializers.CharField(max_length=1000, required=True)

  def create(self, validated_data):
    # Once the request data has been validated, we can create a todo item instance in the database
    return Todo.objects.create(
      text=validated_data.get('text')
    )

  def update(self, instance, validated_data):
     # Once the request data has been validated, we can update the todo item instance in the database
    instance.text = validated_data.get('text', instance.text)
    instance.save()
    return instance

  class Meta:
    model = Todo
    fields = (
      'id',
      'text'
    )


class ServiceCatalogSerializer(serializers.ModelSerializer):
  class Meta:
      model = ServiceCatalog
      fields = ('id', 'name')

class ServiceRequestSerializer(serializers.ModelSerializer):
  service_id = ServiceCatalogSerializer ()
  class Meta:
      model = ServiceRequest
      fields = ('id', 'text', 'creation_date', 'last_updated', 'name', 'last_name','mobile_no','service_id')

class ServiceCatalogSerializer2(serializers.ModelSerializer):
  class Meta:
      model = ServiceCatalog
      fields = ('id', 'name' ,'creation_date', 'last_updated')

class ServiceRequestSerializer2(serializers.ModelSerializer):
  # service_id = ServiceCatalogSerializer ()
  class Meta:
      model = ServiceRequest
      fields = ('id', 'text', 'creation_date', 'last_updated', 'name', 'last_name','mobile_no','service_id')
    
