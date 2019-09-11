# api/urls.py
from django.urls import include, path

urlpatterns = [
    path('usuarios/', include('usuario.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('cuentas/',include('cuenta.urls')),
]