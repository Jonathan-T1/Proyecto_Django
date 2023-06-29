from django import forms
from django.contrib.auth.forms import UserCreationForm
from Users.models import User

class CustumUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','cedula','phone','email', 'password1', 'password2','is_staff','is_profesor','is_Estudiante','is_active']

class editarUser (forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','cedula','phone','email','is_staff','is_profesor','is_Estudiante','is_active']