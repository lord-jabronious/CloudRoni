# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-01 05:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CloudRoni', '0016_userplayer_league'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userplayer',
            name='player_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CloudRoni.Team'),
        ),
    ]
