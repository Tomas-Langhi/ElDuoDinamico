from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser


options = [
    ('entrenador', 'Entrenador'),
    ('jugador', 'Jugador'),
]

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=150, help_text='Email')
    rol = forms.ChoiceField(required=True, widget = forms.Select, choices= options, help_text='rol')

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name',
                  'email', 'rol', 'password1', 'password2',)