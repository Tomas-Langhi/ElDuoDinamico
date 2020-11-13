# -- coding: utf-8 --
from django.contrib import admin
from TeamAdmin.models import *


class PartidoInline(admin.TabularInline):
    model = Partido

class PuntoAdmin(admin.ModelAdmin):
    inlines = [PartidoInline, ]





# Register your models here.


admin.site.register(Posicion,)
admin.site.register(Deporte, )
admin.site.register(Entrenador, )
admin.site.register(Jugador, )
admin.site.register(Equipo, )
admin.site.register(Punto, )
admin.site.register(Partido, )
admin.site.register(Entrenamiento, )
admin.site.register(Tipo, )
admin.site.register(Evento, )
