from django import forms
from .models import *

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CategoriaForm(ModelForm):
    class Meta:
      model = Categoria
      fields = "__all__"
      
class RegistroForm(UserCreationForm):
    username = forms.CharField(max_length=20, help_text="Ingrese su nombre de usuario")
    first_name = forms.CharField(max_length=20, help_text="Ingrese su nombre")
    last_name = forms.CharField(max_length=20, help_text="Ingrese su apellido")
    email = forms.EmailField(max_length=100, help_text="Ingrese su Email")
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }