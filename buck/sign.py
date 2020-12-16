from django.forms import ModelForm
from django import forms
from .models import Sign


class Signin(ModelForm):
    class Meta:
        model = Sign
        fields = ('Username', 'Email', 'Password')
        widgets = {
            'Username': forms.TextInput(attrs={'class': 'form-control np-shadow-inverse p-hover-inverse mb-3', 'placeholder': 'Username', 'type': 'text', 'style': "color: black;"}),
            'Email': forms.EmailInput(attrs={'class': 'form-control np-shadow-inverse p-hover-inverse mb-3', 'placeholder': 'Email', 'type': 'email', 'style': "color: black;"}),
            'Password': forms.PasswordInput(attrs={'class': 'form-control form-control-success np-shadow-inverse p-hover-inverse mb-3', 'type': 'password', 'placeholder': 'Password', 'style': "color: black;"}),
        }
