from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class RegisterForm(UserCreationForm):
    captcha = CaptchaField()
    email = forms.EmailField()
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']


class AuthForm(AuthenticationForm):
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ['__all__']