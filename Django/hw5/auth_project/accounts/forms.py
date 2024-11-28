from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class StandardLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Логін"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Пароль"})
    )


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Ваше ім’я"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Пароль"})
    )
    remember_me = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={"class": "remember-me"})
    )
