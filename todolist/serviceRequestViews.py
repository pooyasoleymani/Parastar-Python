from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from .models import ServiceRequest
from .serializers import ServiceRequestSerializer ,ServiceRequestSerializer2
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.core import serializers
from django.http import HttpResponse

from rest_framework.response import Response

class ServiceRequestView(
  APIView, # Basic View class provided by the Django Rest Framework
  UpdateModelMixin, # Mixin that allows the basic APIView to handle PUT HTTP requests
  DestroyModelMixin, # Mixin that allows the basic APIView to handle DELETE HTTP requests
 ):
#  authentication_classes = [TokenAuthentication]
#  permission_classes = [IsAuthenticated]
 
  def get(self, request, id=None):
    
    if id:
      # If an id is provided in the GET request, retrieve the Todo item by that id
      try:
        # Check if the todo item the user wants to update exists
        queryset = ServiceRequest.objects.filter(id=id)
        requestmy = ServiceRequest.objects.select_related('service_id')
        serialized_data = serializers.serialize('json', requestmy, use_natural_foreign_keys=True)
      
      # Serialize list of todos item from Django queryset object to JSON formatted data
        read_serializer = ServiceRequestSerializer(queryset, many=True)
      except ServiceRequest.DoesNotExist:
        # If the todo item does not exist, return an error response
        return Response({'errors': 'This todo item does not exist.'}, status=400)
      # Return a HTTP response object with the list of todo items as JSON
      return Response(read_serializer.data)

    else:
      # Get all todo items from the database using Django's model ORM
      queryset = ServiceRequest.objects.all()
      requestmy = ServiceRequest.objects.select_related('service_id')
      serialized_data = serializers.serialize('json', requestmy, use_natural_foreign_keys=True)
      
      # Serialize list of todos item from Django queryset object to JSON formatted data
      read_serializer = ServiceRequestSerializer(queryset, many=True)
     
    # Return a HTTP response object with the list of todo items as JSON
      return Response(read_serializer.data)

    

  def post(self, request):
    # Pass JSON data from user POST request to serializer for validation
    create_serializer = ServiceRequestSerializer2(data=request.data)

    # Check if user POST data passes validation checks from serializer
    if create_serializer.is_valid():

      # If user data is valid, create a new todo item record in the database
      todo_item_object = create_serializer.save()

      # Serialize the new todo item from a Python object to JSON format
      read_serializer = ServiceRequestSerializer2(todo_item_object)

      # Return a HTTP response with the newly created todo item data
      return Response(read_serializer.data, status=201)

    # If the users POST data is not valid, return a 400 response with an error message
    return Response(create_serializer.errors, status=400)


  def put(self, request, id=None):
    try:
      # Check if the todo item the user wants to update exists
      todo_item = ServiceRequest.objects.get(id=id)

    except ServiceRequest.DoesNotExist:
      # If the todo item does not exist, return an error response
      return Response({'errors': 'This todo item does not exist.'}, status=400)

    # If the todo item does exists, use the serializer to validate the updated data
    update_serializer = ServiceRequestSerializer2(todo_item, data=request.data)

    # If the data to update the todo item is valid, proceed to saving data to the database
    if update_serializer.is_valid():

      # Data was valid, update the todo item in the database
      todo_item_object = update_serializer.save()

      # Serialize the todo item from Python object to JSON format
      read_serializer = ServiceRequestSerializer2(todo_item_object)

      # Return a HTTP response with the newly updated todo item
      return Response(read_serializer.data, status=200)

    # If the update data is not valid, return an error response
    return Response(update_serializer.errors, status=400)


  def delete(self, request, id=None):
    try:
      # Check if the todo item the user wants to update exists
      todo_item = ServiceRequest.objects.get(id=id)
    except ServiceRequest.DoesNotExist:
      # If the todo item does not exist, return an error response
      return Response({'errors': 'This todo item does not exist.'}, status=400)

    # Delete the chosen todo item from the database
    todo_item.delete()

    # Return a HTTP response notifying that the todo item was successfully deleted
    return Response(status=204)
  

########### only this  Methode requride token #################3
  def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        self.authentication_classes = []
        self.permission_classes = []
# #########  with request type 
#   def dispatch(self, request, *args, **kwargs):
#         if request.method == 'GET':
#             self.authentication_classes = [TokenAuthentication]
#             self.permission_classes = [IsAuthenticated]
#         else:
#             self.authentication_classes = []
#             self.permission_classes = []
#         return super().dispatch(request, *args, **kwargs)
  
#   ######### with metode name ###############3
#   def dispatch(self, request, *args, **kwargs):
#         method_name = self.request.method.lower()
#         if method_name == 'get':
#             self.authentication_classes = [TokenAuthentication]
#             self.permission_classes = [IsAuthenticated]
#         else:
#             self.authentication_classes = []
#             self.permission_classes = []
#         return super().dispatch(request, *args, **kwargs) 