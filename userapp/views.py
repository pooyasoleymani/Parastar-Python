from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class CreateUserView(APIView):
    def get(self, request,id=None):
        if id==None:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        
        users = User.objects.filter(id=id)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
           
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        if not username or not password:
            return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create the user
        user = User.objects.create_user(username=username, password=password, email=email)

        return Response({'message': 'User created successfully.', 'user_id': user.id}, status=status.HTTP_201_CREATED)


class CreateToken(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print("i am here")
        user = User.objects.get(username=username)

        if user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            #token = Token.objects.create(user=user)  this code generate Duplicate error 
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
def retrieve_user(token):
    try:
        token_obj = Token.objects.get(key=token)
        user = token_obj.user
        return user
    except Token.DoesNotExist:
        return None 