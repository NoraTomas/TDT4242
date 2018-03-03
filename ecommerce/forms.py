from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    """Form for getting input needed for registering a new user."""
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
