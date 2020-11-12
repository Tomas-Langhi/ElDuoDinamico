from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    options = [
        ('entrenador', 'Entrenador'),
        ('jugador', 'Jugador'),
    ]
    rol = models.CharField(max_length=3, choices=options, default="jugador")
