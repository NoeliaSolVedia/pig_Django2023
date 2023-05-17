from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index, name='inicio'),
    path('eventos/',views.eventos,name='eventos'),
    path('atractivos/',views.atractivos,name="atractivos"),
    path('registro/',views.registro,name="registro"),
    path('noticias/',views.atractivos,name="noticias"),
]