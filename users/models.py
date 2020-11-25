from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser, UserManager
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, email, rol, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not username:
            raise ValueError('The given username must be set')

        username = self.model.normalize_username(username)
        email = self.normalize_email(email)
        rol = self.get(rol)
        user = self.model(username=username,email=email, rol=rol,  **extra_fields)


        user.set_password(password)
        print("Usando el safe del CustomUserManager...")
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        print("Creating User custom!!")
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        print("Creating SuperUser custom!!")
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)



class User(AbstractUser):
    options = [
        ('entrenador', 'Entrenador'),
        ('jugador', 'Jugador'),
    ]

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(max_length=150, help_text='Email')
    rol = models.ChoiceField(required=True, widget = models.Select, choices= options, help_text='rol')
    date_joined = models.DateTimeField(_('Fecha de creación'), default=timezone.now)

    active = models.BooleanField(_('Activo'), default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)















    # Se establece el manejador del modelo

    objects = CustomUserManager()

    EMAIL_FIELD = email
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'rol']

    class Meta:
        verbose_name = _('usuario')
        verbose_name_plural = _('usuarios')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '{}, {}'.format(self.last_name, self.first_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    get_full_name.short_description = "Full name"

    def __str__(self):
        """
        Returns the full name in a string
        """
        return self.get_full_name()

    def get_rol(self):
        return self.rol


