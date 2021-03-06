# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 03:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivitiesRecord',
            fields=[
                ('activity_id', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('access_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('game_name', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('cost_per_time', models.IntegerField()),
                ('game_description', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_ssn', models.CharField(max_length=200, unique=True)),
                ('user_level', models.IntegerField()),
                ('user_balance', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('transaction_amount', models.IntegerField()),
                ('transaction_date', models.DateField()),
                ('transaction_type', models.CharField(max_length=200)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User_Management.MyUser')),
            ],
        ),
        migrations.AddField(
            model_name='activitiesrecord',
            name='game_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User_Management.Game'),
        ),
        migrations.AddField(
            model_name='activitiesrecord',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User_Management.MyUser'),
        ),
    ]
