from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from django.http import JsonResponse,HttpResponse
from .models import Todo
from .serializers import TodoSerializer
from django.core import serializers


class TodoListView(
  APIView, # Basic View class provided by the Django Rest Framework
  UpdateModelMixin, # Mixin that allows the basic APIView to handle PUT HTTP requests
  DestroyModelMixin, # Mixin that allows the basic APIView to handle DELETE HTTP requests
):

  def get(self, request, id=None):
    
    if id: # check id if not None.
      """
        GET function give id and if in Todo Response JSON to user 
      """
      # check id exist in Todo
      try:
        Todo.objects.get(id=id)
        response = TodoSerializer(Todo.objects.filter(id=id),many=True)
      # if id not exist in Todo
      except Exception:
        return HttpResponse("{'errors': 'This todo item does not exist.'}", status=400)
      
      return Response(response.data)
    # if id is None Response all Todo in JSON 
    response = TodoSerializer(Todo.objects.all(),many=True)
    # js = serializers.serialize('json',response)  
    return Response(response.data)
  
  def post(self, request):
    # Pass JSON data from user POST request to serializer for validation
    create_serializer = TodoSerializer(data=request.data)

    # Check if user POST data passes validation checks from serializer
    if create_serializer.is_valid():

      # If user data is valid, create a new todo item record in the database
      todo_item_object = create_serializer.save()

      # Serialize the new todo item from a Python object to JSON format
      read_serializer = TodoSerializer(todo_item_object)

      # Return a HTTP response with the newly created todo item data
      return Response(read_serializer.data, status=201)

    # If the users POST data is not valid, return a 400 response with an error message
    return Response(create_serializer.errors, status=400)


  def put(self, request, id=None):
    try:
      # Check if the todo item the user wants to update exists
      todo_item = Todo.objects.get(id=id)

    except Todo.DoesNotExist:
      # If the todo item does not exist, return an error response
      return Response({'errors': 'This todo item does not exist.'}, status=400)

    # If the todo item does exists, use the serializer to validate the updated data
    update_serializer = TodoSerializer(todo_item, data=request.data)

    # If the data to update the todo item is valid, proceed to saving data to the database
    if update_serializer.is_valid():

      # Data was valid, update the todo item in the database
      todo_item_object = update_serializer.save()

      # Serialize the todo item from Python object to JSON format
      read_serializer = TodoSerializer(todo_item_object)

      # Return a HTTP response with the newly updated todo item
      return Response(read_serializer.data, status=200)

    # If the update data is not valid, return an error response
    return Response(update_serializer.errors, status=400)


  def delete(self, request, id=None):
    try:
      # Check if the todo item the user wants to update exists
      todo_item = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
      # If the todo item does not exist, return an error response
      return Response({'errors': 'This todo item does not exist.'}, status=400)

    # Delete the chosen todo item from the database
    todo_item.delete()

    # Return a HTTP response notifying that the todo item was successfully deleted
    return Response(status=204)
  