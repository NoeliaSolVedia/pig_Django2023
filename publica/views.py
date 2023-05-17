# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.template import loader

from publica.forms import ConsultaForm, RegistroForm


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

def eventos(request):
    lista_eventos = [
        {  'nombre':'Toreo de la Vincha',
           'fecha_evento':'15/08/2023',
           'descripcion':'Celebración de la fiesta patronal en Honor a la Virgen de la Asunción en donde se realizan actividades tradicionales tales como el baile de los Samilantes y el Toreo de la Vincha.', 
           'direccion':'Casabindo - Dpto. Cochinoca',  
           'imagen_evento':'/static/img/toreo_vincha.jpg',            
        },
        {  'nombre':'Día de la Pachamama',
           'fecha_evento':'1/08/2023',
           'descripcion':'Tradición ancenstral, herencia de los pueblos originarios, donde se entregan en un pozo que representa la boca de la Madre Tierra las ofrendas acompañadas de agradecimientos, rezos y pedidos.', 
           'direccion':'Puesta de Hornillo - Maimarpa',  
           'imagen_evento':'/static/img/pachamama.jpg',            
        },
        {  'nombre':'Fiesta Nacional de los Estudiantes',
           'fecha_evento':'21/09/2023',
           'descripcion':'Inicia con el desfile Bienvenida Primavera y continua con los tradicionales desfiles de carrozas confeccionadas por los estudiantes secundarios y culminan con la elección de la Reina Nacional de los Estudiantes.', 
           'direccion':'Ciudad Cultural - San Salvador de Jujuy',  
           'imagen_evento':'/static/img/fne.png',            
        },
        {  'nombre':'Festival Folclorico del Huancar',
           'fecha_evento':'01/03/2023',
           'descripcion':'Festival para toda la familia donde se realiza el encuentro de comidas regionales, festival de la jineteada y diferentes espectáculos de artistas locales.', 
           'direccion':'Cerro Huancar - Abra Pampa',  
           'imagen_evento':'/static/img/huancar.jpg',            
        },
        {  'nombre':'Carnaval',
           'fecha_evento':'18/02/2023',
           'descripcion':'Celebración popular que inicia en cada comunidad con el desentierro del diablo y las comparsas realizan las invitaciones, bailando carnavalitos por las calles, a los diferentes bailes que se organizan con musica, comida y bebidas tipicas', 
           'direccion':'Quebrada de Humahuaca',  
           'imagen_evento':'/static/img/carnaval.png',            
        },
    ]
    return render(request,'publica/eventos.html',{'lista_eventos':lista_eventos})



def atractivos(request):    
    return render(request,'publica/atractivos.html')

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


