from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from administracion.models import Guia, Turista, Atractivo, Evento, Consulta
from django.forms import ModelChoiceField

# Register your models here.

class PF12AdminSite(admin.AdminSite):
    site_header = "Administración IRPAÑA"
    site_title = "Administración para Super Usuarios"
    index_title = "Administrador del Sitio"
    empty_value_display = "No hay datos para visualizar"

class GuiaAtractivoInline(admin.TabularInline):
     model = Atractivo.guia.through
     extra = 1  # cuantas opciones de carga aparecen por defecto

class GuiaAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre')
    #list_display_links = ('nombre', 'apellido', )
    #list_editable = ('nombre','apellido')
    list_filter = ('apellido',)
    search_fields = ('nombre','apellido')
    #fields = (('nombre', 'apellido'), 'email')  # Si no hacemos un valor editable debe manejarse dicha situación de alguna manera.
    # exclude = ('baja',)
    inlines = (GuiaAtractivoInline, )

    #modificacion del listado que se quiere mostrar
    def get_queryset(self, request):
        query = super(GuiaAdmin, self).get_queryset(request)
        filtered_query = query.filter(baja=False)
        return filtered_query
    
class AtractivoAdmin(admin.ModelAdmin):
    inlines = (GuiaAtractivoInline, )
    # para evitar doble carga
    exclude = ('guia', )

class TuristaAdmin(admin.ModelAdmin):
    list_display = ('apellido','nombre')
    list_filter = ('apellido',)
    search_fields = ('nombre','apellido')

    def get_queryset(self, request):
        query = super(TuristaAdmin, self).get_queryset(request)
        filtered_query = query.filter(baja=False)
        return filtered_query
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "consulta":
            try:
                modelo_a_id = request.resolver_match.args[0]
                modelo_a = Turista.objects.get(id=modelo_a_id)
                kwargs["queryset"] = Consulta.objects.filter(consulta__email=modelo_a.email)
            except (IndexError, ValueError, Turista.DoesNotExist):
                pass
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ( 'fecha_consulta','email','nombre','apellido')



sitio_admin = PF12AdminSite(name='PF12Admin')
""" sitio_admin.register(Guia, GuiaAdmin)
sitio_admin.register(Turista, TuristaAdmin)
sitio_admin.register(Atractivo, AtractivoAdmin)
sitio_admin.register(Consulta, ConsultaAdmin)
sitio_admin.register(Evento)
sitio_admin.register(User, UserAdmin)
sitio_admin.register(Group, GroupAdmin)
 """
admin.site.register(Guia, GuiaAdmin)
admin.site.register(Turista, TuristaAdmin)
admin.site.register(Atractivo, AtractivoAdmin)
admin.site.register(Consulta, ConsultaAdmin)
admin.site.register(Evento)

