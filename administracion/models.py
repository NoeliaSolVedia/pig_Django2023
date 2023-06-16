from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Evento(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripción')
    direccion = models.TextField(verbose_name='Dirección')
    fecha_evento = models.DateField(verbose_name='Fecha de evento')
    imagen_evento = models.ImageField(upload_to='imagenes/',verbose_name='Foto del evento')

    class Meta():
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return self.nombre
    
    def delete(self,using=None,keep_parents=False):
        self.imagen_evento.storage.delete(self.imagen_evento.name) #borrado fisico
        super().delete()

class Consulta(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    apellido = models.CharField(max_length=100,verbose_name='Apellido')
    email = models.EmailField(max_length=100)
    mensaje = models.TextField(verbose_name='Mensaje')  
    fecha_consulta = models.DateField(verbose_name='Fecha de consulta', null=True)

    class Meta():
        verbose_name_plural = 'Consultas'

    def __str__(self):
         return f"{self.fecha_consulta} {self.email}"
    
    def save(self):
        self.fecha_consulta=datetime.date.today()
        super().save()


# USO DE HERENCIA - SOLUCION 3
class Persona(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    apellido = models.CharField(max_length=100,verbose_name='Apellido')
    email = models.EmailField(max_length=100)
    baja = models.BooleanField(default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()
    
class Turista(Persona):
    ATRACTIVOS = [
        (1, "Naturales"),
        (2, "Culturales"),
        (3, "Religiosos"),
        (4, "Deportivos"),
        (5, "Todos"),
    ]
    nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    pais = models.CharField(max_length=50,verbose_name='País')
    ciudad = models.CharField(max_length=100,verbose_name='Ciudad')
    atractivos = models.IntegerField(choices=ATRACTIVOS,default=1)
    aceptar = models.BooleanField(default=0)
    consulta = models.ForeignKey(Consulta,on_delete=models.CASCADE,null=True) #relacion uno a muchos
    
    class Meta():
        verbose_name_plural = 'Turistas'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Guia(Persona):
    especialidad = models.CharField(max_length=150,verbose_name='Especialidad')
    foto = models.ImageField(upload_to='imagenes/',null=True,verbose_name='Foto')

    class Meta():
        verbose_name_plural = 'Guias'
    
    def delete(self,using=None,keep_parents=False):
        self.foto.storage.delete(self.foto.name) #borrado fisico
        super().delete()

class Atractivo(models.Model):
    nombre = models.CharField(max_length=100,verbose_name="Nombre")
    tipo = models.CharField(max_length=100,verbose_name="Atractivo")
    ubicacion = models.TextField(verbose_name='Ubicación')
    imagen_atractivo = models.ImageField(upload_to='imagenes/',verbose_name='Foto del atractivo')
    guia = models.ManyToManyField(Guia) #relacion muchos a muchos

    class Meta():
        verbose_name_plural = 'Atractivos'

    def __str__(self):
        return self.nombre
    
    def delete(self,using=None,keep_parents=False):
        self.imagen_atractivo.storage.delete(self.imagen_atractivo.name) #borrado fisico
        super().delete()

