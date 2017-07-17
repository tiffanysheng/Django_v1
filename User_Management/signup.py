from django import forms
from User_Management.models import User


class NewUser(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'
