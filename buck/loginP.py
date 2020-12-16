from django.forms import ModelForm
from django import forms
from .models import Login


class LoginPage(ModelForm):
    class Meta:
        model = Login
        fields = ('Email', 'Password',)
        widgets = {
            'Email': forms.EmailInput({'class': 'form-control np-shadow-inverse p-hover-inverse mb-3', 'type': 'Email', 'placeholder': 'Email'}),
            'Password': forms.PasswordInput({'class': 'form-control np-shadow-inverse p-hover-inverse mb-3', 'placeholder': 'Password', 'type': 'password'}),
        }
