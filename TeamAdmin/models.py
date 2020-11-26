# -- coding: utf-8 --
from django.db import models
from users.models import CustomUser
# Create your models here.

class Posicion(models.Model):
    nombre = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.nombre

class Deporte(models.Model):
    nombre = models.CharField(max_length=20, default="")
    posicion = models.ForeignKey(Posicion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Entrenador(models.Model):
    usuario = models.ForeignKey(CustomUser, null = True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20, default="")
    apellido = models.CharField(max_length=20, default="")
    dni = models.CharField(max_length=20, default="")
    telefono = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.nombre


class Jugador(models.Model):
    usuario = models.ForeignKey(CustomUser, null = True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20, default="")
    apellido = models.CharField(max_length=20, default="")
    dni = models.CharField(max_length=20, default="")
    telefono = models.CharField(max_length=20, default="")
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=20, default="")
    jugadores = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    entrenadores = models.ForeignKey(Entrenador, on_delete=models.CASCADE)
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Punto(models.Model):
    valor = models.IntegerField()
    minuto = models.CharField(max_length=20, default="")
    tiempo = models.CharField(max_length=20, default="")
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.jugador) + ", " + str(self.valor)


"""
class Partido(models.Model):
    contrincante = models.CharField(max_length=20, default="")
    punto = models.ManyToManyField(Punto)
    puntoContrincante = models.IntegerField()
    puntoEquipo = models.IntegerField()

    def __str__(self):
        return "Partido vs " + str(self.contrincante)

class Entrenamiento(models.Model):
    descripcion = models.CharField(max_length=200, default="")

    def __str__(self):
        return "Entrenamiento " + str(self.descripcion)

class Tipo(models.Model):
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE, blank=True)
    entrenamiento = models.ForeignKey(Entrenamiento, default=None, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return "Evento: " + str(self.partido) + str(self.entrenamiento)
"""
options = [
        ('e', 'Entrenamiento'),
        ('p', 'Partido'),
        ('r', 'Reunion de equipo')
    ]

class Evento(models.Model):
    nombre = models.CharField(max_length=20, default="")
    tipo = models.CharField(max_length=15, choices = options, default = 'e')
    fecha = models.DateField()
    horaInicio = models.TimeField()
    horaFin = models.TimeField() 
    asistencia = models.ManyToManyField(Jugador, default=None)
    descripcion = models.CharField(max_length=200, default="", blank=True)

    # Caracteristicas del partido
    contrincante = models.CharField(max_length=20, default="", blank=True)
    punto = models.ForeignKey(Punto, blank=True, null=True, on_delete=models.CASCADE)
    puntoContrincante = models.IntegerField(default = 0, blank=True)
    puntoEquipo = models.IntegerField(default = None, blank=True)

    def __str__(self):
        return "Evento: " + str(self.nombre)
