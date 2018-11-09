from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse


from .forms import formularioLogin
from django.contrib import messages

from django.urls import reverse


def loginPage(request):
    if request.method =='POST':
        formulario= formularioLogin(request.POST)
        if formulario.is_valid():
            usuario= request.POST['username']
            clave =request.POST['password']
            user= authenticate(username=usuario,password=clave)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('usuarios'))
                    messages.warning(request, 'Ingreso correctamente')

                else:
                    messages.warning(request,'Usuario inactivo')
            else:
                messages.warning(request,'Usuario y/o contraseña inactiva')

    else:
        formulario=formularioLogin()

    context={
        'f': formulario,
    }
    return render(request,'login/login.html',context)


def logoutPage(request):
    logout(request)
    return HttpResponseRedirect(reverse('home_page'))