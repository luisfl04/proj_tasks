from django import forms
from .models import DadosRegistro


class RegisterForm(forms.ModelForm):

    class Meta:

        model = DadosRegistro
        fields = [
            "first_name",
            "last_name",
            "age",
            "username",
            "email",
            "password",
        ]

class LoginForm(forms.ModelForm):

    class Meta:

        model = DadosRegistro
        fields = [
            "username",
            "password"
        ]