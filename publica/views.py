# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.template import loader

from publica.forms import ConsultaForm, RegistroForm
# from publica.forms_registro import RegistroForm


from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):    
    mensaje="Mensaje de prueba"
    if(request.method=='POST'):
        consulta_form = ConsultaForm(request.POST)
        if(consulta_form.is_valid()):  
            messages.success(request,'Hemos recibido tus datos y te responderemos a la brevedad.')          
            consulta_form = ConsultaForm() #reset formulario
            # acción para tomar los datos del formulario
        else:
            messages.warning(request,'Por favor revisa los errores en el formulario.')
    else:
        consulta_form = ConsultaForm()
    return render(request,'publica/index.html',{
                    'mensaje': mensaje,
                    'consulta_form': consulta_form})

def quienes_somos(request):
    template = loader.get_template('publica/quienes_somos.html')
    context = {'titulo':'Quienes Somos'}
    return HttpResponse(template.render(context,request))


def atractivos(request):    
    return render(request,'publica/atractivos.html')

# def registro(request):
#     if request.method == "POST":
#         # Creao la instancia populada con los datos cargados en pantalla
#         registro_form = RegistroForm(request.POST)
#         # Valido y proceso los datos.
#         if registro_form.is_valid():
#             # messages.set_level(request, messages.DEBUG)
#             messages.success(request, "Formulario cargado con éxito")
#             # messages.debug(request, "DEBUGG")
#             # messages.info(request, "Info importante")
#             # messages.warning(request, "Algo anda mal")
#             # messages.error(request, "NO ANDA")
#     else:
#         # Creo el formulario vacío con los valores por defecto
#         registro_form = RegistroForm()
#     return render(request, "publica/registro.html", {'registro_form': registro_form})

def registro(request):
    mensaje="Mensaje de prueba"
    if request.method == "POST":
        # Creao la instancia populada con los datos cargados en pantalla
        registro_form = RegistroForm(request.POST)
        # Valido y proceso los datos.
        if registro_form.is_valid():
            # messages.set_level(request, messages.DEBUG)
            messages.success(request, "Formulario cargado con éxito")
            registro_form = RegistroForm(request.POST)
            # messages.debug(request, "DEBUGG")
            # messages.info(request, "Info importante")
            # messages.warning(request, "Algo anda mal")
            # messages.error(request, "NO ANDA")
        else:
            messages.warning(request,'Por favor revisa los errores en el formulario.')
    else:
        # Creo el formulario vacío con los valores por defecto
        registro_form = RegistroForm()
    return render(request,'publica/registro.html',{
                    'mensaje': mensaje,
                    'registro_form': registro_form})



def noticias(request):    
    return render(request,'publica/noticias.html')


