from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrarUsuarioForm(UserCreationForm):
    username = forms.CharField(
            label='Usuario', 
            widget=forms.TextInput(attrs={'placeholder':'Ingrese nombre de Usuario'})
        )
    password1 = forms.CharField(
            label='Password1', 
            widget=forms.TextInput(attrs={'placeholder':'Ingrese su contraseña'})
        )
    password2 = forms.CharField(
            label='Password2', 
            widget=forms.TextInput(attrs={'placeholder':'Confirme la contraseña'})
        )
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']