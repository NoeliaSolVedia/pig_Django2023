from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index_administracion,name='inicio_administracion'),

    path('eventos/', views.eventos_index,name='eventos_index'),
    path('eventos/nuevo/', views.eventos_nuevo,name='eventos_nuevo'),
    path('eventos/editar/<int:id_evento>', views.eventos_editar,name='eventos_editar'),
    path('eventos/eliminar/<int:id_evento>', views.eventos_eliminar,name='eventos_eliminar'),

    path('guias/', views.guias_index,name='guias_index'),
    path('guias/nuevo/', views.guias_nuevo,name='guias_nuevo'),
    path('guias/editar/<int:id_guia>', views.guias_editar,name='guias_editar'),
    path('guias/eliminar/<int:id_guia>', views.guias_eliminar,name='guias_eliminar'),
]
