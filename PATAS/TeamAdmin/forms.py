from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    nombre = forms.CharField(max_length=100, help_text='Nombre')
    apellido = forms.CharField(max_length=100, help_text='Apellido')
    email = forms.EmailField(max_length=150, help_text='Email')

    class Meta:
        model = User
        fields = ('username', 'nombre', 'apellido',
                  'email', 'password1', 'password2',)