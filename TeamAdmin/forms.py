from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=150, help_text='Email')

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2',)