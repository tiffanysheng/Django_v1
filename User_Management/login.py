from django import forms
from django.core import validators


class FormLogin(forms.Form):
    username = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'style':'width:40%'}))
    password = forms.CharField(max_length=200,widget=forms.PasswordInput(attrs={'style':'width:40%'}))

