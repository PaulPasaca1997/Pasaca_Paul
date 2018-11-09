from django.shortcuts import render,redirect
from modelo.models import Usuario
from .forms import FormularioUsuario

def principal (request):

    listaUsuarios = Usuario.objects.all().order_by('apellidos')
    context = {
            'lista': listaUsuarios
        }

    return render(request, 'principal.html', context)

def crear (request):
    formulario = FormularioUsuario(request.POST)
    if request.method == 'POST':
        if formulario.is_valid():
            datos = formulario.cleaned_data        #arreglo de todos los datos q tiene el formulario
            usuario = Usuario()
            usuario.cedula = datos.get('cedula');
            usuario.numero_matricula = datos.get('numero_matricula');
            usuario.apellidos = datos.get('apellidos');
            usuario.nombres = datos.get('nombres');
            usuario.proveniencia = datos.get('proveniencia');
            usuario.carrera = datos.get('carrera');
            usuario.trabaja = datos.get('trabaja');
            usuario.save()
            return redirect(principal)


    context = {
        'f': formulario,
        'mensaje':'Bienvenido',
    }
    return render(request, 'crear_usuario.html', context)




