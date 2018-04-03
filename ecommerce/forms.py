from django import forms
from django.contrib.auth.models import User
from .models import Category


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class CategorySearchForm(forms.Form):
    categoryOptions = [c for c in Category.objects.all()]

    Categories = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=categoryOptions, required=False)

