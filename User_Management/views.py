from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import login
from User_Management.signup import NewUser, MyUserForm
from django.contrib import auth
from django.core.urlresolvers import reverse
from User_Management.models import MyUser
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models


def index(request):
    form = login.FormLogin()
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
    form = login.FormLogin()
    state = None
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            if user.is_superuser == True:
                return HttpResponseRedirect("admin")
            else:
                return HttpResponseRedirect("User_Management/user_page")
        else:
            state = 'not_exist_or_password_error'
            return render(request, 'login.html', {'form': form, 'state': state})

    return render(request, 'login.html', {'form' : form, 'state':state})


def logOut(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('logIn'))


def showUserPage(request):
    return render(request, 'user_page.html', {'user_fullname':request.user.get_full_name,'user':request.user.id})


class UserInfoDetailView(DetailView):
    context_object_name = 'user_info'
    model = models.MyUser
    template_name = 'user_info.html'


def showUserActivity(request):
    return render(request, 'user_activity.html')