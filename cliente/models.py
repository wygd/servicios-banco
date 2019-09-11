from django.db import models

# Create your models here.
class Cliente(models.Model):
	nombre_usuario = models.CharField(max_length=30)
	email = models.EmailField(max_length=70,blank=True)
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	password = models.CharField(max_length=100)
	telefono = models.CharField(max_length=10)