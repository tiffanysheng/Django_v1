from django.contrib import admin
from User_Management.models import MyUser, Game, Transaction, ActivitiesRecord

# Register your models here.
class ActivitiesRecordAdmin(admin.ModelAdmin):
    list_display = ['activity_id','user_id','access_date']


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['transaction_id','user_id','transaction_date']


class GameAdmin(admin.ModelAdmin):
    list_display = ['game_name']


admin.site.register(MyUser)
admin.site.register(Game, GameAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(ActivitiesRecord, ActivitiesRecordAdmin)
