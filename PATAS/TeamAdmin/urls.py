from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('servicios/', servicio, name="servicios"),
    path('contacto/', contacto, name="contacto"),
    path('signUp/', signup_view, name="signUp"),
]

