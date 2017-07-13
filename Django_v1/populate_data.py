'''import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_v1.settings')

import django

django.setup()

import random
from User_Management.models import User,Game,Transaction,ActivitiesRecord
from faker import Faker

fakegen = Faker()

def populate(N=10):

    for entry in range(N):

        fake_user_id = fakegen.ssn()
        fake_user_name = fakegen.name()
        fake_user_password = fakegen.password(length=8)
        fake_user_level = 1
        fake_user_balance = 1000

        user = User.objects.get_or_create(user_id=fake_user_id,user_name=fake_user_name,user_password=fake_user_password,user_level=fake_user_level,user_balance=fake_user_balance)[0]

        #fake_game_name = ['Poker','Blackjack','Roulette','Baccarat','Craps','Keno','Casino War','Slots']
        fake_game_name = fakegen.company()
        fake_cost_per_time = 100
        fake_game_description = fakegen.text(max_nb_chars=100)

        game = Game.objects.get_or_create(game_name=fake_game_name,cost_per_time=fake_cost_per_time,game_description=fake_game_description)[0]

        fake_activity_id = fakegen.ssn()
        fake_access_date = fakegen.date_time()

        activity = ActivitiesRecord(activity_id=fake_activity_id,user_id=user,access_date=fake_access_date,game_name=game)



if __name__ == '__main__':
    populate(10)
'''