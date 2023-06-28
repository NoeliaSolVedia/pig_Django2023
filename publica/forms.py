from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError
from administracion.models import Turista, Consulta

def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('El nombre no puede contener números. %(valor)s',
                              code='Error1',
                              params={'valor': value})
    
class RegistrarUsuarioForm(UserCreationForm):
    username = forms.CharField(
            label='Usuario', 
            widget=forms.TextInput(attrs={'placeholder':'Ingrese nombre de Usuario'})
        )
    password1 = forms.CharField(
            label='Password1',
            widget=forms.PasswordInput(attrs={'placeholder':'Ingrese su contraseña'})
        )

    password2 = forms.CharField(
            label='Password2', 
            widget=forms.PasswordInput(attrs={'placeholder':'Confirme su contraseña'})
        )
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class TuristaForm(forms.ModelForm):
    ATRACTIVOS = [
        (1, "Naturales"),
        (2, "Culturales"),
        (3, "Religiosos"),
        (4, "Deportivos"),
        (5, "Todos"),
    ]
    nombre = forms.CharField(
            label='NOMBRE:',
            max_length=50,
            validators=(solo_caracteres,),
            widget=forms.TextInput(attrs={'placeholder':''})
    )
    apellido = forms.CharField(
            label='APELLIDO:',
            max_length=50,
            validators=(solo_caracteres,),
            widget=forms.TextInput(attrs={'placeholder':''})
    )
    email = forms.EmailField(
            label='EMAIL:',
            max_length=100,
            widget=forms.TextInput(attrs={'type':'email'})
    )
    nacimiento = forms.DateField(
        label='FECHA DE NACIMIENTO:',
        widget=forms.DateInput(attrs={'type':'date'})
    )
    pais = forms.CharField(
            label='PAÍS:',
            max_length=50,
            validators=(solo_caracteres,),
            widget=forms.TextInput(attrs={'placeholder':''})
    )
    ciudad = forms.CharField(
            label='CIUDAD:',
            max_length=50,
            validators=(solo_caracteres,),
            widget=forms.TextInput(attrs={'placeholder':''})
    )
    atractivos = forms.ChoiceField(
        label='Indique los atractivos en que esta interesad@:',
        required=True,
        choices=ATRACTIVOS,
        initial=1
    )
    aceptar = forms.BooleanField(
            required=True,
            label='He leído y acepto los términos y condiciones de uso.',
            error_messages={'required': 'Debes leer y aceptar nuestro términos y condiciones de uso. '},
            widget=forms.CheckboxInput(attrs={'class':'form-control','value':1})
    )

    class Meta:
        model=Turista
        fields=['nombre','apellido','email','nacimiento','pais','ciudad','atractivos','aceptar']
        exclude = ['consulta']

class ConsultaForm(forms.Form):
    nombre = forms.CharField(
            label='Nombre', 
            max_length=50,
            required=True,
            validators=(solo_caracteres,),
            widget=forms.TextInput(attrs={'placeholder':''})
        )
    apellido = forms.CharField(
            label='Apellido', 
            max_length=50,
            required=True,
            validators=(solo_caracteres,),
            widget=forms.TextInput(attrs={'placeholder':''})
        )
    email = forms.EmailField(
            label='Email',
            max_length=100,
            required=True,
            error_messages={'required': 'Por favor coloca un correo electrónico.',},
            widget=forms.TextInput(attrs={'type':'email'})
        )
    mensaje = forms.CharField(
        label='Mensaje',
        max_length=500,
        error_messages={'required': 'Por favor ingresa tu consulta'},
        widget=forms.Textarea(attrs={'rows': 5,})
    )

    def clean_mensaje(self):
        data = self.cleaned_data['mensaje']
        if len(data) < 10:
            raise ValidationError("Debes especificar mejor la consulta que nos envias")
        return data
