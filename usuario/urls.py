# users/urls.py
from django.urls import include, path

from usuario.views import UserListView

urlpatterns = [
    path('lista_usuarios',UserListView.as_view()),
]