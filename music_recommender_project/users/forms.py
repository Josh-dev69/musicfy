from django.contrib.auth import login, authenticate
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username or Email")

    class Meta:
        fields = ["username", "password"]