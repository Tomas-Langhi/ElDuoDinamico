from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'TeamAdmin/home.html')


def servicio(request):
    return render(request, 'TeamAdmin/servicios.html')


def contacto(request):
    return render(request, 'TeamAdmin/contacto.html')


"""
def login(request):
    return render(request, 'registration/login.html')
"""


def register(request):
    print("entreo 1")

    data = {
        'form': SignUpForm()
    }

    if request.method == 'POST':

        print("paso el primer if")

        formulario = SignUpForm(request.POST)

        print("soy hermoso")

        if formulario.is_valid():

            print("paso el segundo if")

            formulario.save()

            # inicia sesion y redirige al inicio

            username = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            print("ESTO SI FUNCIONA ----------------------------------------------")

            return redirect('/')

    else:
        
        form = SignUpForm()

        print("ESTO NO FUNCIONA ----------------------------------------------")

    return render(request, "TeamAdmin/register.html", data)


