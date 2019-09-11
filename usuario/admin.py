from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from usuario.forms import CustomUserCreationForm, CustomUserChangeForm
from usuario.models import Usuario

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Usuario
    list_display = ['email', 'username', 'nombre','apellido','tipo_usuario']

admin.site.register(Usuario, CustomUserAdmin)