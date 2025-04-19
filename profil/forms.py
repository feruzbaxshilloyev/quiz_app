from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'name', 'last_name', 'phone', 'address', 'image']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
