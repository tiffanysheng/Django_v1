# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitiesrecord',
            name='activity_cost',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
