from django.contrib import admin

from .models import Usuario


# Register your models here.
class AdminUsuario(admin.ModelAdmin):
    list_display = ["cedula","numero_matricula","nombres","apellidos","proveniencia","carrera","trabaja"]
    list_editable = ["apellidos", "nombres"]
    search_fields = ["cedula"]
    #search_fields = ["cedula"],"apellidos","nombre"]

    class Meta:
        model = Usuario


admin.site.register(Usuario, AdminUsuario)