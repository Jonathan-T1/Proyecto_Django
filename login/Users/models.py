from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser,PermissionsMixin
from core import *

# Create your models here.
class User(AbstractUser,AbstractBaseUser,PermissionsMixin):
    picture = models.ImageField(default='imagen_base.png',upload_to='users/', verbose_name='Foto De Perfil', null=True)
    cedula = models.CharField(max_length=11, verbose_name='Cedula', blank=False, help_text=(
        "Obligatorio. Digite su nemero de Cedula completo. Unicamente numeros. Sin puntos ni comas"
    ))
    phone = models.CharField(max_length=10, verbose_name='Celuar', blank=False, help_text=(
        "Obligatorio. Digite su nemero de Celular completo. Unicamente numeros. Sin puntos ni comas"
    ))
    is_profesor = models.BooleanField(
        ("Rol Profesor"),
        default=False
    )
    is_Estudiante = models.BooleanField(
        ("Estudiante"),
        default=False
    )
