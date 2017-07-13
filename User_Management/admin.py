from django.contrib import admin
from User_Management.models import User, Game, Transaction, ActivitiesRecord

# Register your models here.
admin.site.register(User)
admin.site.register(Game)
admin.site.register(Transaction)
admin.site.register(ActivitiesRecord)
