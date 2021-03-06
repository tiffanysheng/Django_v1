from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class MyUser(models.Model):
    user = models.OneToOneField(User)
    """
    user_id = models.CharField(max_length=200, unique=True, primary_key=True)
    user_name = models.CharField(max_length=100)
    user_password = models.CharField(max_length=200)
    """
    id = models.AutoField(primary_key=True)
    user_ssn = models.CharField(max_length=200, unique=True)
    user_level = models.IntegerField()
    user_balance = models.IntegerField()

    def __str__(self):
        return self.user.username


class Game(models.Model):
    game_name = models.CharField(max_length=200, unique=True, primary_key=True)
    cost_per_time = models.IntegerField()
    game_description = models.CharField(max_length=400)

    def __str__(self):
        return self.game_name


class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(MyUser)
    transaction_amount = models.IntegerField()
    transaction_date = models.DateField(auto_now_add=True)
    transaction_type = models.CharField(max_length=200)

    def __str__(self):
        return str(self.transaction_id)


class ActivitiesRecord(models.Model):
    activity_id = models.AutoField(primary_key=True)
    access_date = models.DateField(auto_now_add=True)
    user_id = models.ForeignKey(MyUser)
    game_name = models.ForeignKey(Game)
    activity_cost = models.IntegerField()

    def __str__(self):
        return str(self.activity_id)
