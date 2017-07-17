from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from . import login
from User_Management.signup import NewUser
from django.contrib import auth
from django.core.urlresolvers import reverse


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


def logIn(request):
    form = login.FormLogin();
    state = None
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("")
        else:
            state = 'not_exist_or_password_error'
            return render(request, 'login.html', {'form': form, 'state': state})

    return render(request, 'login.html', {'form' : form, 'state':state})


def logOut(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('logIn'))