from django.conf.urls import url
from User_Management import views


app_name = 'User_Management'

urlpatterns=[
    url(r'^signup/$',views.signup,name='signup'),
]