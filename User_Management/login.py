from django import forms


class FormLogin(forms.Form):
    id = forms.CharField()
    pw = forms.CharField()

print("dasd")