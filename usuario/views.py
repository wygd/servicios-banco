#from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from usuario import models
from usuario import serializers

class UserListView(generics.ListCreateAPIView):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UserSerializer