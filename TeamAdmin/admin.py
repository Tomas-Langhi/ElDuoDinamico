# -- coding: utf-8 --
from django.contrib import admin
from TeamAdmin.models import *


class EventoInline(admin.TabularInline):
    model = Evento

class PuntoAdmin(admin.ModelAdmin):
    inlines = [EventoInline, ]

class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'fecha')
    search_fields = ['tipo', 'fecha', 'nombre']
    # filter_horizontal = ['tipo', 'fecha', 'nombre']

    fieldsets = (
        ("Evento", {
            'fields': ('nombre', 'tipo', 'fecha', 'horaInicio', 'horaFin', 'asistencia', 'descripcion',)
        }),
        ("Partido", {
            'fields': ('contrincante', 'punto', 'puntoContrincante', 'puntoEquipo')
        }),
    )

# Register your models here.


admin.site.register(Posicion,)
admin.site.register(Deporte, )
admin.site.register(Entrenador, )
admin.site.register(Jugador, )
admin.site.register(Equipo, )
admin.site.register(Punto,)
admin.site.register(Evento, EventoAdmin)
