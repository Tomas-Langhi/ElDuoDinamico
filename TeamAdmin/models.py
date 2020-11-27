# -- coding: utf-8 --
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Posicion(models.Model):
    nombre = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.nombre

class Deporte(models.Model):
    nombre = models.CharField(max_length=20, default="")
    

    def __str__(self):
        return self.nombre

class Entrenador(models.Model):
    #nombre_usuario = models.CharField(max_length=20, default="", help_text="Ingrese su nombre de usuario")
    nombre = models.CharField(max_length=20, default="")
    apellido = models.CharField(max_length=20, default="")
    #mail = models.EmailField(max_length=20, default="")
    #contraseña = models.CharField(max_length=20, default="", help_text="Ingrese su contraseña")
    dni = models.CharField(max_length=20, default="")
    telefono = models.CharField(max_length=20, default="")
    
    """
    @classmethod
    def guardar_jugador(self):
        print("entra aca PERO NO FUNCIONA")
        user = User.objects.create_user(self.nombre_usuario, self.mail, self.contraseña)
        user.first_name = self.nombre
        user.last_name = slef.apellido
        user.save()
        return user
    """

    def __str__(self):
        return self.nombre


class Jugador(models.Model):
    usuario = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20, default="")
    apellido = models.CharField(max_length=30, default="")
    dni = models.CharField(max_length=20, default="")
    telefono = models.CharField(max_length=20, default="")
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    posicion = models.ForeignKey(Posicion, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Punto(models.Model):
    valor = models.IntegerField()
    minuto = models.CharField(max_length=20, default="")
    tiempo = models.CharField(max_length=20, default="")
    jugador = models.ForeignKey(Jugador, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.jugador) + ", " + str(self.valor)


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
    contrincante = models.CharField(max_length=20, default="", blank=True, null = True)
    punto = models.ForeignKey(Punto, blank=True, null=True, on_delete=models.CASCADE)
    puntoContrincante = models.IntegerField(default = 0, blank=True, null = True)
    puntoEquipo = models.IntegerField(default = None, blank=True, null = True)

    def __str__(self):
        return "Evento: " + str(self.nombre)
