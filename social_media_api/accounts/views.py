from django.shortcuts import render
from .models import CustomUser
from rest_framework import generics
from .serializers import RegisterSerializer, UserSerializer
# Create your views here.


from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserSerializer, RegisterSerializer

from rest_framework import generics
from .serializers import RegisterSerializer, UserSerializer
from .models import CustomUser

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    # Login logic here
    pass

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    # You can add permissions here to restrict access to authenticated users only

