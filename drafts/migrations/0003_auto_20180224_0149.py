# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-24 01:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drafts', '0002_auto_20180224_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draft',
            name='current_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CloudRoni.Team'),
        ),
    ]