from django.shortcuts import render
from . import login
# Create your views here.


def index(request):
    form = login.FormLogin();
    return render(request, 'login.html', {'form' : form})


