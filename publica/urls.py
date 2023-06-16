from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [    
    path('', views.index, name='inicio'),
    path('cuentas/registrarse', views.registrarse, name='registrarse'),
    path('cuentas/login', views.iniciar_sesion, name='iniciar_sesion'),
    path('cuentas/logout/',
         auth_views.LogoutView.as_view(template_name='publica/index.html'), name='logout'),

    path('guias_model/',views.guias_model,name='guias_model'),
    path('atractivos_model/',views.atractivos_model,name="atractivos_model"),
    path('registro/',views.registro,name="registro"),
    path('agenda_model/',views.agenda_model,name="agenda_model"),
    path('info/',views.info,name="info"),
]