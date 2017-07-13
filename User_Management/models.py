from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=200, unique=True, primary_key=True)
    user_name = models.CharField(max_length=100)
    user_password = models.CharField(max_length=200)
    user_level = models.IntegerField()
    user_balance = models.IntegerField()

    def __str__(self):
        return self.user_id


class Game(models.Model):
    game_name = models.CharField(max_length=200, unique=True, primary_key=True)
    cost_per_time = models.IntegerField()
    game_description = models.CharField(max_length=400)

    def __str__(self):
        return self.game_name


class Transaction(models.Model):
    transaction_id = models.CharField(max_length=200, unique=True, primary_key=True)
    user_id = models.ForeignKey(User)
    transaction_amount = models.IntegerField()
    transaction_date = models.DateField()
    transaction_type = models.CharField(max_length=200)

    def __str__(self):
        return self.transaction_id


class ActivitiesRecord(models.Model):
    activity_id = models.CharField(max_length=200, unique=True, primary_key=True)
    access_date = models.DateField()
    user_id = models.ForeignKey(User)
    game_name = models.ForeignKey(Game)

    def __str__(self):
        return self.activity_id
