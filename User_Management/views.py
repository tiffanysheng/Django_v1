from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import login
from User_Management.signup import NewUser, MyUserForm
from django.contrib import auth
from django.core.urlresolvers import reverse
from User_Management.models import MyUser
from django.views.generic import View, TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . import models
from User_Management.permission import PermissionVerify
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q
from douban.models import Books


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
    print(request.user.myuser.id)
    return render(request, 'user_page.html', {'user_fullname':request.user.get_full_name,'myuser_id':request.user.myuser.id})


class UserInfoDetailView(DetailView):
    context_object_name = 'user_info'
    model = models.MyUser
    template_name = 'user_info.html'

    def get_context_data(self, **kwargs):
        context = super(UserInfoDetailView, self).get_context_data(**kwargs)
        context['user_fullname'] = self.request.user.get_full_name
        context['myuser_id'] = self.request.user.myuser.id
        return context

    @method_decorator(PermissionVerify)
    def dispatch(self, *args, **kwargs):
        return super(UserInfoDetailView, self).dispatch(*args, **kwargs)


class UserActivityListView(ListView):
    model = models.ActivitiesRecord
    context_object_name = 'user_activities'
    template_name = 'user_activity.html'

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q=="" or q==None:
            return models.ActivitiesRecord.objects.filter(user_id_id=self.request.user.myuser.id).order_by('-access_date')
        else:
            return models.ActivitiesRecord.objects.filter(Q(user_id_id=self.request.user.myuser.id), (Q(game_name__game_name__icontains=q) | Q(activity_id__icontains=q))).order_by('-access_date')
            #return models.ActivitiesRecord.objects.filter(user_id_id=self.request.user.myuser.id,game_name__game_name__icontains=q).order_by('-access_date')

    def get_context_data(self, **kwargs):
        context = super(UserActivityListView, self).get_context_data(**kwargs)
        context['user_fullname'] = self.request.user.get_full_name
        context['myuser_id'] = self.request.user.myuser.id
        context['filtername'] = self.request.GET.get('q')
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserActivityListView, self).dispatch(*args, **kwargs)


class UserTransListView(ListView):
    model = models.Transaction
    context_object_name = 'user_transactions'
    template_name = 'user_transaction.html'

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q == "" or q == None:
            return models.Transaction.objects.filter(user_id_id=self.request.user.myuser.id).order_by('-transaction_date')
        else:
            return models.Transaction.objects.filter(Q(user_id_id=self.request.user.myuser.id), (Q(transaction_id__icontains=q) | Q(transaction_type__icontains=q))).order_by('-transaction_date')

    def get_context_data(self, **kwargs):
        context = super(UserTransListView, self).get_context_data(**kwargs)
        context['user_fullname'] = self.request.user.get_full_name
        context['myuser_id'] = self.request.user.myuser.id
        context['filtername'] = self.request.GET.get('q')
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserTransListView, self).dispatch(*args, **kwargs)


def addActivity(request, userid, gamename):
    game = models.Game.objects.get(game_name__exact=gamename)
    user = models.MyUser.objects.get(id=userid)
    models.ActivitiesRecord.objects.create(user_id=user, game_name=game, activity_cost=game.cost_per_time)
    return HttpResponseRedirect(reverse('logIn'))


def addTransaction(request, userid, transamount, transtype):
    user = models.MyUser.objects.get(id=userid)
    models.Transaction.objects.create(user_id=user, transaction_amount=transamount, transaction_type=transtype)
    return HttpResponseRedirect(reverse('logIn'))


class BooksListView(ListView):
    model = Books
    context_object_name = 'spider_books'
    template_name = 'user_page.html'

    def get_queryset(self):
        return Books.objects.using('spiderdb').values('name','author','score','isbn','price').order_by('-score')

    def get_context_data(self, **kwargs):
        context = super(BooksListView, self).get_context_data(**kwargs)
        context['user_fullname'] = self.request.user.get_full_name
        context['myuser_id'] = self.request.user.myuser.id
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BooksListView, self).dispatch(*args, **kwargs)
