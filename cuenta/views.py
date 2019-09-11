# Create your views here.
#from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from cuenta import models
from cuenta import serializers

class CuentaListView(generics.ListCreateAPIView):
    queryset = models.Cuenta.objects.all()
    serializer_class = serializers.CuentaSerializer