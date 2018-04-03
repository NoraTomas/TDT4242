from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

class HomeForm(forms.Form):
    post = forms.CharField(required=False, widget=forms.NumberInput)
