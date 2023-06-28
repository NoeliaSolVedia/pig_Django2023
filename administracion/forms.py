from django import forms
from django.forms import ValidationError
from administracion.models import Evento, Guia, Turista, Consulta, Atractivo
from django.forms import ClearableFileInput

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
            widget=forms.DateInput(attrs={'class':'form-control'}, format='%d-%m-%Y'), input_formats=['%d-%m-%Y']
        )
    descripcion = forms.CharField(
        label='Descripción',
        widget=forms.Textarea(attrs={'rows': 5,'class':'form-control'})
    )
    direccion=forms.CharField(
            label='Dirección', 
            widget=forms.TextInput(attrs={'class':'form-control'})
    )
    imagen_evento = forms.ImageField(widget=ClearableFileInput(attrs={'multiple': False}))
    
    class Meta:
        model=Evento
        fields=['nombre','fecha_evento','descripcion','direccion','imagen_evento']

class AtractivoForm(forms.ModelForm):
    nombre=forms.CharField(
            label='Nombre', 
            widget=forms.TextInput(attrs={'class':'form-control'})
        )
    tipo=forms.CharField(
            label='Tipo', 
            widget=forms.TextInput(attrs={'class':'form-control'})
        )
    ubicacion= forms.CharField(
        label='Ubicación',
        widget=forms.Textarea(attrs={'rows': 5,'class':'form-control'})
    )
    imagen_atractivo = forms.ImageField(widget=ClearableFileInput(attrs={'multiple': False}))

    class Meta:
        model=Atractivo
        fields=['nombre','tipo','ubicacion','imagen_atractivo']

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
            widget=forms.Textarea(attrs={'rows': 5,'class':'form-control'})
    )
    foto = forms.ImageField(widget=ClearableFileInput(attrs={'multiple': False}))
    
    class Meta:
        model=Guia
        fields=['nombre','apellido','email','especialidad','foto']

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
            widget=forms.TextInput(attrs={'class':'form-control'})
    )
    apellido = forms.CharField(
            label='APELLIDO:',
            max_length=50,
            validators=(solo_caracteres,),
            widget=forms.TextInput(attrs={'class':'form-control'})
    )
    email = forms.EmailField(
            label='EMAIL:',
            max_length=100,
            widget=forms.TextInput(attrs={'type':'email','class':'form-control'})
    )
    nacimiento = forms.DateField(
        label='FECHA DE NACIMIENTO:',
        widget=forms.DateInput(attrs={'class':'form-control'}, format='%d-%m-%Y'), input_formats=['%d-%m-%Y']
    )
    pais = forms.CharField(
            label='PAÍS:',
            max_length=50,
            validators=(solo_caracteres,),
            widget=forms.TextInput(attrs={'class':'form-control'})
    )
    ciudad = forms.CharField(
            label='CIUDAD:',
            max_length=50,
            validators=(solo_caracteres,),
            widget=forms.TextInput(attrs={'class':'form-control'})
    )
    atractivos = forms.ChoiceField(
        label='Indique los atractivos en que esta interesad@:',
        required=True,
        choices=ATRACTIVOS,
        initial=1,
    )

    class Meta:
        model=Turista
        fields=['nombre','apellido','email','nacimiento','pais','ciudad','atractivos','consulta']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   
        if self.instance.pk:
          email = self.instance.email
          self.fields['consulta'].queryset = Consulta.objects.filter(email=email)


class ConsultaForm(forms.ModelForm):
    nombre = forms.CharField(
            label='Nombre', 
            max_length=50,
            validators=(solo_caracteres,),
            widget=forms.TextInput(attrs={'class':'form-control'})
        )
    apellido = forms.CharField(
            label='Apellido', 
            max_length=50,
            validators=(solo_caracteres,),
            widget=forms.TextInput(attrs={'class':'form-control'})
        )
    email = forms.EmailField(
            label='Email',
            max_length=100,
            widget=forms.TextInput(attrs={'type':'email','class':'form-control'})
        )
    mensaje = forms.CharField(
        label='Mensaje',
        max_length=500,
        error_messages={'required': 'Por favor ingresa tu consulta'},
        widget=forms.Textarea(attrs={'rows': 5,'class':'form-control'}) 
    )
    fecha_consulta = forms.DateField(
        label='FECHA DE CONSULTA:',
        widget=forms.DateInput(attrs={'class':'form-control'}, format='%d-%m-%Y'), input_formats=['%d-%m-%Y']
    )

    def clean_mensaje(self):
        data = self.cleaned_data['mensaje']
        if len(data) < 10:
            raise ValidationError("Debes especificar mejor la consulta que nos envias")
        return data
    
    class Meta:
        model=Consulta
        fields=['nombre','apellido','email','mensaje','fecha_consulta']
        #exclude = ['fecha_consulta']
