from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
=======

>>>>>>> 3d8244905c494fdc8f9b9df9bed87ba52b17a72e

def home(request):
    return render(request, 'TeamAdmin/home.html')


def servicio(request):
    return render(request, 'TeamAdmin/servicios.html')


def contacto(request):
    return render(request, 'TeamAdmin/contacto.html')

<<<<<<< HEAD
=======
def sign_in_view(request):
    return render(request, 'registration/login.html')
>>>>>>> 3d8244905c494fdc8f9b9df9bed87ba52b17a72e

def signup_view(request):
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
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
<<<<<<< HEAD
    return render(request, "TeamAdmin/signup_view.html", {'form': form})


=======
    return render(request, "registration/register.html", data)
>>>>>>> 3d8244905c494fdc8f9b9df9bed87ba52b17a72e
