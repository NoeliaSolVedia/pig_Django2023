import os
from django.conf import settings

from administracion.models import Evento, Guia, Atractivo, Consulta, Turista
from administracion.forms import EventoForm, GuiaForm, AtractivoForm, ConsultaForm, TuristaForm

from django.views.generic import ListView
from django.urls import reverse_lazy
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.
@login_required
def index_administracion(request):
    variable = 'test variable'
    return render(request,'administracion/index_administracion.html',
                  {'variable':variable})

"""   CRUD Eventos   """
@login_required
def eventos_index(request):
    message=""
    if request.method == 'POST':
        name = request.POST['nombre_buscado']
        if name=="":
            message = 'Debe ingresar un valor para la búsqueda.'
            eventos = Evento.objects.all()
        else:
            eventos = Evento.objects.filter(nombre__icontains=name)
        page = request.GET.get('page',1)
        try:
            paginator = Paginator(eventos,4)
            eventos = paginator.page(page)
        except:
            raise Http404
        if not eventos:
            message = 'El registro no fue encontrado.'
            # Si no se encontró un registro válido, mostrar un mensaje de error al usuario
        return render(request, 'administracion/eventos/index.html', {'entity':eventos, 'message': message, 'paginator':paginator})
    else:
        eventos = Evento.objects.all()
        page = request.GET.get('page',1)
        try:
            paginator = Paginator(eventos,4)
            eventos = paginator.page(page)
        except:
            raise Http404
    return render(request,'administracion/eventos/index.html',{'entity':eventos, 'message': message, 'paginator':paginator})

def eventos_nuevo(request):
    if(request.method=='POST'):
        formulario = EventoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('eventos_index')
    else:
        formulario = EventoForm()
    return render(request,'administracion/eventos/nuevo.html',{'form':formulario})

def eventos_editar(request,id_evento):
    try:
        evento = Evento.objects.get(pk=id_evento)
        foto_actual = evento.imagen_evento.name
    except Evento.DoesNotExist:
        return render(request,'administracion/404_admin.html')

    if(request.method=='POST'):
        formulario = EventoForm(request.POST,request.FILES, instance=evento)
        if formulario.is_valid():
            # Verificar si el campo de imagen ha cambiado
            if 'imagen_evento' in request.FILES and evento.imagen_evento:
                # Eliminar el archivo anterior de la imagen
                os.remove(os.path.join(settings.MEDIA_ROOT,foto_actual))
            formulario.save()
            return redirect('eventos_index')
    else:
        formulario = EventoForm(instance=evento)
    return render(request,'administracion/eventos/editar.html',{'form':formulario})

def eventos_eliminar(request,id_evento):
    try:
        evento = Evento.objects.get(pk=id_evento)
    except Evento.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    evento.delete()
    return redirect('eventos_index')

"""   CRUD Atractivos   """
@login_required
def atractivos_index(request):
    message=""
    if request.method == 'POST':
        name = request.POST['nombre_buscado']
        if name=="":
            message = 'Debe ingresar un valor para la búsqueda.'
            atractivos = Atractivo.objects.all()
        else:
            atractivos = Atractivo.objects.filter(nombre__icontains=name)
        page = request.GET.get('page',1)
        try:
            paginator = Paginator(atractivos,4)
            atractivos = paginator.page(page)
        except:
            raise Http404
        if not atractivos:
            message = 'El registro no fue encontrado.'
            # Si no se encontró un registro válido, mostrar un mensaje de error al usuario
        return render(request, 'administracion/atractivos/index.html', {'entity':atractivos, 'message': message, 'paginator':paginator})
    else:
        atractivos = Atractivo.objects.all()
        page = request.GET.get('page',1)
        try:
            paginator = Paginator(atractivos,4)
            atractivos = paginator.page(page)
        except:
            raise Http404
    return render(request,'administracion/atractivos/index.html',{'entity':atractivos, 'message': message, 'paginator':paginator})

class AtractivosListView(ListView):
    model = Atractivo
    context_object_name = 'atractivos'
    template_name= 'administracion/atractivos/index.html'
    queryset= Atractivo.objects.all()
   # ordering = ['nombre']
    #paginate_by = 5

def atractivos_nuevo(request):
    if(request.method=='POST'):
        formulario = AtractivoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('atractivos_index')
    else:
        formulario = AtractivoForm()
    return render(request,'administracion/atractivos/nuevo.html',{'form':formulario})

def atractivos_editar(request,id_atractivo):
    try:
        atractivo = Atractivo.objects.get(pk=id_atractivo)
        foto_actual = atractivo.imagen_atractivo.name
    except Atractivo.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    if(request.method=='POST'):
        formulario = AtractivoForm(request.POST,request.FILES, instance=atractivo)
        if formulario.is_valid():
             # Verificar si el campo de imagen ha cambiado
            if 'imagen_atractivo' in request.FILES and atractivo.imagen_atractivo:
                # Eliminar el archivo anterior de la imagen
                os.remove(os.path.join(settings.MEDIA_ROOT,foto_actual))
            formulario.save()
            return redirect('atractivos_index')
    else:
        formulario = AtractivoForm(instance=atractivo)
    return render(request,'administracion/atractivos/editar.html',{'form':formulario})

def atractivos_eliminar(request,id_atractivo):
    try:
        atractivo = Atractivo.objects.get(pk=id_atractivo)
    except Atractivo.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    atractivo.delete()
    return redirect('atractivos_index')

"""     CRUD GUIAS     """
@login_required
def guias_index(request):
    message=""
    guias=""
    if request.method == 'POST':
        nombre = request.POST.get('nombre_buscado', '')
        apellido = request.POST.get('apellido_buscado', '')
        if (len(nombre)==1 and len(apellido)==1):
            guias = Guia.objects.filter(Q(nombre__startswith=nombre) & Q(apellido__startswith=apellido)).filter(baja=False)
        elif len(nombre)==1:
            guias = Guia.objects.filter(nombre__startswith=nombre).filter(baja=False)
        elif len(apellido)==1:
            guias = Guia.objects.filter(apellido__startswith=apellido).filter(baja=False)
        else:
          if nombre and apellido:
            # Si se ingresaron ambos valores, buscar registros que contengan el nombre y el apellido
            guias = Guia.objects.filter(Q(nombre__icontains=nombre) | Q(apellido__icontains=apellido)).filter(baja=False)
          elif nombre:
            # Si solo se ingresó el nombre, buscar registros que contengan el nombre
            guias = Guia.objects.filter(nombre__icontains=nombre).filter(baja=False)
          elif apellido:
            # Si solo se ingresó el apellido, buscar registros que contengan el apellido
            guias = Guia.objects.filter(apellido__icontains=apellido).filter(baja=False)
          else:
            message = 'Debe ingresar un valor para la búsqueda o la inicial del nombre y/o apellido.'
            guias = Guia.objects.all().filter(baja=False)
        page = request.GET.get('page',1)
        try:
            paginator = Paginator(guias,4)
            guias = paginator.page(page)
        except:
            raise Http404
        if not guias:
            message = 'El registro no fue encontrado.'
            # Si no se encontró un registro válido, se mostrara un mensaje de error al usuario
        return render(request, 'administracion/guias/index.html', {'entity':guias, 'message': message, 'paginator':paginator})
    else:
        guias = Guia.objects.all().filter(baja=False)
        page = request.GET.get('page',1)
        try:
            paginator = Paginator(guias,4)
            guias = paginator.page(page)
        except:
            raise Http404
    return render(request,'administracion/guias/index.html',{'entity':guias, 'message': message, 'paginator':paginator})

def guias_nuevo(request):
    if(request.method=='POST'):
        formulario = GuiaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('guias_index')
    else:
        formulario = GuiaForm()
    return render(request,'administracion/guias/nuevo.html',{'form':formulario})

def guias_editar(request,id_guia):
    try:
        guia = Guia.objects.get(pk=id_guia)
        foto_actual = guia.foto.name
    except Guia.DoesNotExist:
        return render(request,'administracion/404_admin.html')

    if(request.method=='POST'):
        formulario = GuiaForm(request.POST,request.FILES, instance=guia)
        if formulario.is_valid():
            # Verificar si el campo de imagen ha cambiado
            if 'foto' in request.FILES and guia.foto:
                # Eliminar el archivo anterior de la imagen
                os.remove(os.path.join(settings.MEDIA_ROOT,foto_actual))
            formulario.save()
            return redirect('guias_index')
    else:
        formulario = GuiaForm(instance=guia)
    return render(request,'administracion/guias/editar.html',{'form':formulario})

def guias_eliminar(request,id_guia):
    try:
        guia = Guia.objects.get(pk=id_guia)
    except Guia.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    guia.soft_delete()
    return redirect('guias_index')


"""     CRUD CONSULTAS     """
@login_required
def consultas_index(request):
    message=""
    consultas=""
    if request.method == 'POST':
        nombre = request.POST.get('nombre_buscado', '')
        apellido = request.POST.get('apellido_buscado', '')
        if (len(nombre)==1 and len(apellido)==1): 
             # Si se ingresó una letra, buscar registros que empiecen con esa letra
            consultas = Consulta.objects.filter(Q(nombre__startswith=nombre) & Q(apellido__startswith=apellido)).filter(baja=False)
        elif len(nombre)==1:
            consultas = Consulta.objects.filter(nombre__startswith=nombre).filter(baja=False)
        elif len(apellido)==1:
            consultas = Consulta.objects.filter(apellido__startswith=apellido).filter(baja=False)
        else:
          if nombre and apellido:
            # Si se ingresaron ambos valores, buscar registros que contengan el nombre y el apellido
            consultas = Consulta.objects.filter(Q(nombre__icontains=nombre) | Q(apellido__icontains=apellido))
          elif nombre:
            # Si solo se ingresó el nombre, buscar registros que contengan el nombre
            consultas = Consulta.objects.filter(nombre__icontains=nombre)
          elif apellido:
            # Si solo se ingresó el apellido, buscar registros que contengan el apellido
            consultas = Consulta.objects.filter(apellido__icontains=apellido)
          else:
            message = 'Debe ingresar un valor para la búsqueda o la inicial del nombre y/o apellido.'
            consultas = Consulta.objects.all()
        page = request.GET.get('page',1)
        try:
            paginator = Paginator(consultas,4)
            consultas = paginator.page(page)
        except:
            raise Http404
        if not consultas:
            message = 'El registro no fue encontrado.'
            # Si no se encontró un registro válido, se mostrara un mensaje de error al usuario
        return render(request, 'administracion/consultas/index.html', {'entity':consultas, 'message': message, 'paginator':paginator})
    else:
        consultas = Consulta.objects.all()
        page = request.GET.get('page',1)
        try:
            paginator = Paginator(consultas,4)
            consultas = paginator.page(page)
        except:
            raise Http404
    return render(request,'administracion/consultas/index.html',{'entity':consultas, 'message': message, 'paginator':paginator})

def consultas_nuevo(request):
    if(request.method=='POST'):
        formulario = ConsultaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('consultas_index')
    else:
        formulario = ConsultaForm()
    return render(request,'administracion/consultas/nuevo.html',{'form':formulario})

def consultas_editar(request,id_consulta):
    try:
        consulta = Consulta.objects.get(pk=id_consulta)
    except Consulta.DoesNotExist:
        return render(request,'administracion/404_admin.html')

    if(request.method=='POST'):
        formulario = ConsultaForm(request.POST,request.FILES, instance=consulta)
        if formulario.is_valid():
            formulario.save()
            return redirect('consultas_index')
    else:
        formulario = ConsultaForm(instance=consulta)
    return render(request,'administracion/consultas/editar.html',{'form':formulario})

def consultas_eliminar(request,id_consulta):
    try:
        consulta = Consulta.objects.get(pk=id_consulta)
    except Consulta.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    consulta.delete()
    return redirect('consultas_index')

"""     CRUD Turista     """
@login_required
def turistas_index(request):
    message=""
    turistas=""
    if request.method == 'POST':
        nombre = request.POST.get('nombre_buscado', '')
        apellido = request.POST.get('apellido_buscado', '')
        if (len(nombre)==1 and len(apellido)==1):
            turistas = Turista.objects.filter(Q(nombre__startswith=nombre) & Q(apellido__startswith=apellido)).filter(baja=False)
        elif len(nombre)==1:
            turistas = Turista.objects.filter(nombre__startswith=nombre).filter(baja=False)
        elif len(apellido)==1:
            turistas = Turista.objects.filter(apellido__startswith=apellido).filter(baja=False)
        else:
          if nombre and apellido:
            # Si se ingresaron ambos valores, buscar registros que contengan el nombre y el apellido
            turistas = Turista.objects.filter(Q(nombre__icontains=nombre) | Q(apellido__icontains=apellido)).filter(baja=False)
          elif nombre:
            # Si solo se ingresó el nombre, buscar registros que contengan el nombre
            turistas = Turista.objects.filter(nombre__icontains=nombre).filter(baja=False)
          elif apellido:
            # Si solo se ingresó el apellido, buscar registros que contengan el apellido
            turistas = Turista.objects.filter(apellido__icontains=apellido).filter(baja=False)
          else:
            message = 'Debe ingresar un valor para la búsqueda o la inicial del nombre y/o apellido.'
            turistas = Turista.objects.all().filter(baja=False)
        page = request.GET.get('page',1)
        try:
            paginator = Paginator(turistas,4)
            turistas = paginator.page(page)
        except:
            raise Http404
        if not turistas:
            message = 'El registro no fue encontrado.'
            # Si no se encontró un registro válido, se mostrara un mensaje de error al usuario
        return render(request, 'administracion/turistas/index.html', {'entity':turistas, 'message': message, 'paginator':paginator})
    else:
        turistas = Turista.objects.all().filter(baja=False)
        page = request.GET.get('page',1)
        try:
            paginator = Paginator(turistas,4)
            turistas = paginator.page(page)
        except:
            raise Http404
    return render(request,'administracion/turistas/index.html',{'entity':turistas, 'message': message, 'paginator':paginator})

def turistas_nuevo(request):
    if(request.method=='POST'):
        formulario = TuristaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('turistas_index')
    else:
        formulario = TuristaForm()
    return render(request,'administracion/turistas/nuevo.html',{'form':formulario})

def turistas_editar(request,id_turista):
    try:
        turista = Turista.objects.get(pk=id_turista)
    except Turista.DoesNotExist:
        return render(request,'administracion/404_admin.html')

    if(request.method=='POST'):
        formulario = TuristaForm(request.POST,request.FILES, instance=turista)
        if formulario.is_valid():
            formulario.save()
            return redirect('turistas_index')
    else:
        formulario = TuristaForm(instance=turista)
    return render(request,'administracion/turistas/editar.html',{'form':formulario, 'turista':turista})

def turistas_eliminar(request,id_turista):
    try:
        turista = Turista.objects.get(pk=id_turista)
    except Turista.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    turista.soft_delete()
    return redirect('turistas_index')
