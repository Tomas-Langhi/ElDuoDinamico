from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate

def home(request):
    return render(request, 'TeamAdmin/home.html')


def servicio(request):
    return render(request, 'TeamAdmin/servicios.html')


def contacto(request):
    return render(request, 'TeamAdmin/contacto.html')

def login(request):
    return render(request, 'TeamAdmin/login.html')

def register(request):
    data = {
        'form': SignUpForm()
    }

    if request.method == 'POST':
        formulario = SignUpForm(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            user.save()

            # inicia sesion y redirige al inicio
            username = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, "TeamAdmin/register.html", data)
