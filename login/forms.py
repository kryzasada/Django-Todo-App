from django import forms
from django.contrib.auth.models import User as usersLogin
from django.contrib.auth.forms import UserCreationForm


class UsersCreationForm(UserCreationForm):
    username = forms.EmailField()

    class Meta:
        model = usersLogin
        fields = [
            'username',
            'password1',
            'password2',
        ]
