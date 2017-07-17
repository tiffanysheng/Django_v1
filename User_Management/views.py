from django.shortcuts import render
from . import login
# Create your views here.
from User_Management.signup import NewUser


def index(request):
    form = login.FormLogin();
    return render(request, 'login.html', {'form' : form})


def signup(request):
    form = NewUser
    if request.method == "POST":
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    return render(request, 'signup.html', {'form':form})
