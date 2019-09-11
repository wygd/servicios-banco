from django.db import models
from usuario.models import Usuario

# Create your models here.
class Cuenta(models.Model):
	numero = models.CharField(max_length=15)
	cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	saldo_actual = models.DecimalField(max_digits=19, decimal_places=10)
	activa = models.BooleanField()

	def __str__(self):
		return self.numero

class TipoTransaccion(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField()
	abono = models.BooleanField(default=True)

	def __str__(self):
		return self.nombre


class Transaccion(models.Model):
	cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
	tipo_transaccion = models.ForeignKey(TipoTransaccion, on_delete=models.CASCADE)
	monto = models.DecimalField(max_digits=19, decimal_places=10)
	#empleado = models.ForeignKey()
	fecha = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return 'Es una transaccion'