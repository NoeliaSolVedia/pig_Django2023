from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index, name='inicio'),
    path('quienes_somos/',views.quienes_somos,name='quienes_somos'),
    path('atractivos/',views.atractivos,name="atractivos"),
    path('registro/',views.registro,name="registro"),
    path('noticias/',views.atractivos,name="noticias"),
]