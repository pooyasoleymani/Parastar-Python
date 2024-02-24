import json
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from rest_framework.serializers import ModelSerializer

# this class for serialized the user model
class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username')

@csrf_exempt
@require_http_methods(['GET','POST'])
# this function response  the user request
def user_request(request,id=None):
    if request.method == 'GET':
        if id==None:
            query = User.objects.all()
            serializer = CreateUserSerializer(query, many=True)

            return JsonResponse(serializer.data, safe=False, status=201)
        
        query = get_object_or_404(User, id=id)
        serializer = CreateUserSerializer(query)
        return JsonResponse(serializer.data, safe=False, status=201)
    
    elif request.method == 'POST':
        body = json.loads(request.body)
        try:
            User.objects.filter(username=body['username'])
            return HttpResponse(f'{body['username']} is exist!')
        except Exception:
            query = User.objects.create_user(username=body['username'],password=body['password'])
            query.save()

            return HttpResponse(f'user is created.')
        
        