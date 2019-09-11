# users/forms.py
from django import forms
from cuenta.models import Cuenta

class CustomCuentaCreationForm(forms.ModelForm):

    class Meta:
        model = Cuenta
        fields = ('cliente','saldo_actual','activa')

class CustomCuentaChangeForm(forms.ModelForm):

    class Meta:
        model = Cuenta
        fields = ('cliente','saldo_actual','activa') 