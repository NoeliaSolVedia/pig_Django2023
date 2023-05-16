from django import forms
from django.forms import ValidationError
from django.core import validators

def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('El nombre no puede contener números: %(valor)s',
                            code='Invalid',
                            params={'valor':value})

# Formulario de consulta:

class ConsultaForm(forms.Form):
    nombre = forms.CharField(
            label='Nombre', 
            max_length=50,
            validators=(solo_caracteres,),
            widget=forms.TextInput(attrs={'placeholder':''})
        )
    apellido = forms.CharField(
            label='Apellido', 
            max_length=50,
            validators=(solo_caracteres,),
            widget=forms.TextInput(attrs={'placeholder':''})
        )
    email = forms.EmailField(
            label='Email',
            max_length=100,
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

# Formulario de registro:

class RegistroForm(forms.Form):
    ATRACTIVOS = [("naturales", "Naturales"),("culturales", "Culturales"),("religiosos", "Religiosos")]

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
        widget=forms.TextInput()
    )
    atractivos = forms.MultipleChoiceField(
        label='Indique sus preferencias:',
        required=False,
        widget=forms.CheckboxSelectMultiple(),
        choices=ATRACTIVOS
    )
    condiciones = forms.BooleanField(
            label='He leído y acepto los términos y condiciones de uso.',
            error_messages={'required': 'Debes leer y aceptar nuestro términos y condiciones de uso. '},
            widget=forms.CheckboxInput(attrs={'class':'form-control','value':1})
    )
  