# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-23 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CloudRoni', '0009_auto_20180123_0116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trade',
            name='proposing_team_player_ids',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='receiving_team_player_ids',
        ),
        migrations.AddField(
            model_name='trade',
            name='proposing_team_players',
            field=models.ManyToManyField(related_name='proposing_team_players', to='CloudRoni.UserPlayer'),
        ),
        migrations.AddField(
            model_name='trade',
            name='receiving_team_players',
            field=models.ManyToManyField(related_name='receiving_team_players', to='CloudRoni.UserPlayer'),
        ),
    ]
