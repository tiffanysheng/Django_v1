from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from . import login
from User_Management.signup import NewUser, MyUserForm
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import user_passes_test, login_required


def index(request):
    form = login.FormLogin();
    return render(request, 'login.html', {'form' : form})


def signup(request):

    signuped = False

    if request.method == "POST":
        form = NewUser(data=request.POST)
        profileform = MyUserForm(data=request.POST)
        if form.is_valid() and profileform.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            profile = profileform.save(commit=False)
            profile.user = user
            profile.save()
            signuped = True
    else:
        form = NewUser()
        profileform = MyUserForm()

    return render(request, 'signup.html', {'form': form,
                                           'profile_form': profileform,
                                           'signuped': signuped})


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