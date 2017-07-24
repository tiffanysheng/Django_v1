from django.conf.urls import url
from User_Management import views
from django.contrib.auth.decorators import login_required, permission_required


app_name = 'User_Management'

urlpatterns=[
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^user_page/$',views.showUserPage,name='user_page'),
    url(r'^logout/$',views.logOut,name='logout'),
    url(r'^user_info/(?P<pk>\d+)/$',views.UserInfoDetailView.as_view(),name='user_info'),
    url(r'^user_activity/$',views.UserActivityListView.as_view(),name='user_activity'),
    url(r'^user_transaction/$',views.UserTransListView.as_view(),name='user_transaction'),
]