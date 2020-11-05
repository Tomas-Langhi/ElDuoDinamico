from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'TeamAdmin/home.html')

def servicio(request):
    return render(request, 'TeamAdmin/servicios.html')

def contacto(request):
    return render(request, 'TeamAdmin/contacto.html')




    

def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        nombre = form.cleaned_data.get('nombre')
        apellido = form.cleaned_data.get('apellido')
        email = form.cleaned_data.get('email')
        rol = form.cleaned_data.get('rol')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        print ("SE GUARDO EL USUARIO")
        return redirect('/')
    else:
        form = SignUpForm()
    return render(request, "TeamAdmin/signup_view.html", {'form': form})


