from django import forms
from django.contrib.auth.models import User
from .models import Item

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

class ItemForm(forms.ModelForm):
    amount = forms.IntegerField(widget=forms.NumberInput)

    class Meta:
        model = Item
        fields = ['amount']