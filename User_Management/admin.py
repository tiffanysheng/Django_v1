from django.contrib import admin
from User_Management.models import MyUser, Game, Transaction, ActivitiesRecord

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Game)
admin.site.register(Transaction)
admin.site.register(ActivitiesRecord)
