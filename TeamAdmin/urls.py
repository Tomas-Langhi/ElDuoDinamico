from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    #path('servicios/', servicio, name="servicios"),
    path('quienesSomos/', quienesSomos, name="contacto"),
    path('register/', register, name="signUp"),
    path('virus/', virus, name="virus"),
]

