# users/serializers.py
from rest_framework import serializers
from cuenta import models
from datetime import datetime


class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cuenta
        extra_kwargs = {'numero': {'read_only': True}}
        fields = ('numero','cliente','saldo_actual','activa')

    def create(self, validated_data):
        """Create and return a new user."""

        cuenta = models.Cuenta(
            cliente = validated_data['cliente'],
            saldo_actual = validated_data['saldo_actual'],
            activa = validated_data['activa'],
        )
        cuenta.save()
        numero_cuenta = datetime.now().strftime('%Y%m%d%H%M%S')
        cuenta.numero = numero_cuenta + str(cuenta.id)
        cuenta.save()
        return cuenta