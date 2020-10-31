from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate

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
        user.profile.nombre = form.cleaned_data.get('nombre')
        user.profile.apellido = form.cleaned_data.get('apellido')
        user.profile.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('')
    else:
        form = SignUpForm()
    return render(request, "TeamAdmin/signup_view.html", {'form': form})
