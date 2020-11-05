from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('servicios/', servicio, name="servicios"),
    path('contacto/', contacto, name="contacto"),
    #path('signIn/', sign_in_view, name="signIn"),
    path('signUp/', signup_view, name="signUp"),
]


