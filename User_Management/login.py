from django import forms


class FormLogin(forms.Form):
    id = forms.CharField()
    password = forms.CharField()
