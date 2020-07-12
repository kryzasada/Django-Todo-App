from django import forms
from .models import usersLogin


class userLoginForm(forms.ModelForm):
    class Meta:
        model = usersLogin
        fields = [
            "email",
            "password",
        ]
