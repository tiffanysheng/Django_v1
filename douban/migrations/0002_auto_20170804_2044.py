# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 20:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('douban', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='books',
            table='Books',
        ),
    ]
