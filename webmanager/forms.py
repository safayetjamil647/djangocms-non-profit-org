from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Blog


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class Blog(forms.ModelForm):
    class Meta:
        model = Blog

        fields = [
            "blog_title",
            "blog_desc"
        ]
