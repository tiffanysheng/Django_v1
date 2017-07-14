from django import forms


class FormLogin(forms.Form):
    id = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'style':'width:40%'}))
    password = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'style':'width:40%'}))
