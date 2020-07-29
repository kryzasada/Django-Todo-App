from django import forms

from .models import UserPost

class UserPostForms(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = [
            'date',
            'text',
            'users',
        ]
