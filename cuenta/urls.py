# users/urls.py
from django.urls import include, path

from cuenta.views import CuentaListView

urlpatterns = [
    path('lista_cuentas',CuentaListView.as_view()),
]