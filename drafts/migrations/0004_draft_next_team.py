# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-25 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drafts', '0003_auto_20180224_0149'),
    ]

    operations = [
        migrations.AddField(
            model_name='draft',
            name='next_team',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
