
from django import forms
from modelo.models import Usuario

class FormularioUsuario(forms.ModelForm):
    class Meta:
        model= Usuario
        fields = ["cedula","numero_matricula", "nombres", "apellidos","proveniencia","carrera","trabaja"]
