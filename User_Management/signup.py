from django import forms
from User_Management.models import MyUser
from django.contrib.auth.models import User


class NewUser(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class MyUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields =('user_ssn', 'user_level', 'user_balance')
