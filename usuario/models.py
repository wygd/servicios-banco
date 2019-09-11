from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):
	TIPOS_USUARIO = (
      (1, 'cliente'),
      (2, 'empleado'),
      (3, 'admin'),
      )
	nombre = models.CharField(blank=True, max_length=255)
	apellido = models.CharField(blank=True, max_length=255)
	tipo_usuario = models.PositiveSmallIntegerField(choices=TIPOS_USUARIO)
	def __str__(self):
		return self.email