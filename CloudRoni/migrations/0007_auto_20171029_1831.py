# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-29 18:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CloudRoni', '0006_auto_20170828_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userplayer',
            name='player_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CloudRoni.Team'),
        ),
    ]