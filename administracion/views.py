from administracion.models import Evento, Guia
from administracion.forms import EventoForm, GuiaForm

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def index_administracion(request):
    variable = 'test variable'
    return render(request,'administracion/index_administracion.html',
                  {'variable':variable})

"""   CRUD Eventos   """

def eventos_index(request):
    #queryset
    eventos = Evento.objects.all()
    return render(request,'administracion/eventos/index.html',{'eventos':eventos})

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
    except Evento.DoesNotExist:
        return render(request,'administracion/404_admin.html')

    if(request.method=='POST'):
        formulario = EventoForm(request.POST,request.FILES, instance=evento)
        if formulario.is_valid():
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


"""     CRUD GUIAS     """

def guias_index(request):
    #queryset
    guias = Guia.objects.all()
    return render(request,'administracion/guias/index.html',{'guias':guias})

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
    except Guia.DoesNotExist:
        return render(request,'administracion/404_admin.html')

    if(request.method=='POST'):
        formulario = GuiaForm(request.POST,request.FILES, instance=guia)
        if formulario.is_valid():
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
    guia.delete()
    return redirect('guias_index')
