from django import forms
from django.forms import ValidationError
from .models import Evento, Guia


def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('El nombre no puede contener números. %(valor)s',
                              code='Error1',
                              params={'valor': value})

class EventoForm(forms.ModelForm):

    nombre=forms.CharField(
            label='Nombre', 
            widget=forms.TextInput(attrs={'class':'form-control'})
        )
    fecha_evento=forms.DateField(
            label='Fecha de Evento', 
            widget=forms.DateInput(attrs={'class':'form-control','type':'date'})
        )
    descripcion = forms.CharField(
        label='Descripción',
        widget=forms.Textarea(attrs={'rows': 5,'class':'form-control'})
    )
    direccion=forms.CharField(
            label='Dirección', 
            widget=forms.TextInput(attrs={'class':'form-control'})
    )
    imagen_evento = forms.ImageField(
        widget=forms.FileInput(attrs={'class':'form-control'})
    )
    
    """Se utiliza ModelChoiceField para poder realizar un filtrado de lo que
    quiero mostrar en el selector
     categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(baja=False),
        widget=forms.Select(attrs={'class': 'form-control'})
    ) """

    class Meta:
        model=Evento
        fields=['nombre','fecha_evento','descripcion','direccion','imagen_evento']

class GuiaForm(forms.ModelForm):
    nombre = forms.CharField(
            label='Nombre', 
            required=True,
            validators=(solo_caracteres,),
            widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Ingrese solo texto'})
    )
    apellido = forms.CharField(
        label='Apellido:',
        required=True,
        validators=(solo_caracteres,),
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ingrese solo texto'})
    )
    email = forms.EmailField(
        label='Email:',
        max_length=50,
        error_messages={
            'required': 'Por favor completa el campo',
        },
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'type': 'email'})
    )
    especialidad = forms.CharField(
            label='Especialidad', 
            widget=forms.TextInput(attrs={'class':'form-control'})
    )
    foto = forms.ImageField(
        widget=forms.FileInput(attrs={'class':'form-control'})
    )
    
    class Meta:
        model=Guia
        fields=['nombre','apellido','email','especialidad','foto']

    