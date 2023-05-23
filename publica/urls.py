from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index, name='inicio'),
    path('guias/',views.guias,name='guias'),
    path('guias_model/',views.guias_model,name='guias_model'),
    path('atractivos/',views.atractivos,name="atractivos"),
    path('registro/',views.registro,name="registro"),
    path('agenda/',views.agenda,name="agenda"),
    path('agenda_model/',views.agenda_model,name="agenda_model"),
]