from django.conf.urls import url
from User_Management import views


app_name = 'User_Management'

urlpatterns=[
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^user_page/$',views.showUserPage,name='user_page'),
    url(r'^logout/$',views.logOut,name='logout'),
    url(r'^user_page/(?P<pk>\d+)/$',views.UserInfoDetailView.as_view(),name='user_info'),
    url(r'^user_activity/$',views.showUserActivity,name='user_activity'),
]