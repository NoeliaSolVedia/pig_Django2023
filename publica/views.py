# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from administracion.forms import TuristaForm, ConsultaForm
from publica.forms import RegistrarUsuarioForm
from administracion.models import Evento, Guia, Atractivo

from datetime import datetime, date
from django.contrib import messages

# Create your views here.
def index(request):    
    mensaje="Mensaje de prueba"
    if(request.method=='POST'):
        consulta_form = ConsultaForm(request.POST)
        if(consulta_form.is_valid()):  
            messages.success(request,'Gracias por contactarte, te responderemos a la brevedad.')          
            consulta_form = ConsultaForm(request.POST) #reset formulario
   #         consulta_form.fields['fecha_consulta'].initial = date.today()
            consulta_form.save()
            # acción para tomar los datos del formulario
        else:
            messages.warning(request,'Por favor revisa los errores en el formulario.')
    else:
        consulta_form = ConsultaForm()
    return render(request,'publica/index.html',{
                    'mensaje': mensaje,
                    'consulta_form': consulta_form})

def registro(request):
    if request.method == "POST":
        # Creao la instancia populada con los datos cargados en pantalla
        registro_form = TuristaForm(request.POST)
        # Valido y proceso los datos.
        if registro_form.is_valid():
            # messages.set_level(request, messages.DEBUG)
            #messages.success(request, "Formulario cargado con éxito")
            registro_form = TuristaForm(request.POST)
            registro_form.save()
            return redirect('registrarse')
            # messages.debug(request, "DEBUGG")
            # messages.info(request, "Info importante")
            # messages.warning(request, "Algo anda mal")
            # messages.error(request, "Error")
        else:
            messages.warning(request,'Por favor revisa los errores en el formulario.')
    else:
        # Creo el formulario vacío con los valores por defecto
        registro_form = TuristaForm()
    return render(request,'publica/formulario.html',{
                    'registro_form': registro_form})


def agenda_model(request):
    #queryset
    lista_queryset = []
    for i in range(1,13):
       queryset = Evento.objects.order_by('fecha_evento').filter(fecha_evento__month=i) # i es el mes que deseamos filtrar
       lista_queryset.append(queryset)
    return render(request,'publica/agenda.html',{'lista_queryset':lista_queryset})

def guias_model(request):
    #queryset
    guias = Guia.objects.all()
    return render(request,'publica/guias.html',{'guias':guias})

def atractivos_model(request):
    #queryset
    atractivos = Atractivo.objects.all()
    return render(request,'publica/atractivos.html',{'atractivos':atractivos})

def registrarse(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Tu cuenta fue creada con éxito! Ya te podes loguear en el sistema.')
            return redirect('iniciar_sesion')
    else:
        form = RegistrarUsuarioForm()
    return render(request, 'publica/registrarse.html', {'form': form, 'title': 'Registro de Usuario'})


def iniciar_sesion(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' Bienvenido/a {username} !!')
            return redirect('inicio')
        else:
            messages.error(request, f'Cuenta o password incorrecto, realice el login correctamente')
    form = AuthenticationForm()
    return render(request, 'publica/login.html', {'form': form, 'title': 'Inicio de Sesion'})


def info(request):
    return render(request,'publica/info.html')