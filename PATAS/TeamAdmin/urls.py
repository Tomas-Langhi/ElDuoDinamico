from django.urls import path
from .views import *
from django.contrib import admin

urlpatterns = [
    path('', home, name="home"),
    path('servicios/', servicio, name="servicios"),
    path('contacto/', contacto, name="contacto"),
    path('signup/', signup_view, name="signup"),
    path('admin/', admin.site.urls),
]


