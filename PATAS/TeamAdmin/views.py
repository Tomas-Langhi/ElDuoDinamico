from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate, get_user


def home(request):
    return render(request, 'TeamAdmin/home.html')


def servicio(request):
    return render(request, 'TeamAdmin/servicios.html')


def contacto(request):
    return render(request, 'TeamAdmin/contacto.html')

def sign_in_view(request):
    return render(request, 'registration/login.html')

def signup_view(request):
    data = {
        'form': SignUpForm()
    }

    if request.method == 'POST':
        formulario = SignUpForm(request.POST)
        if formulario.is_valid():
            formulario.save()

            # inicia sesion y redirige al inicio
            username = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", data)
