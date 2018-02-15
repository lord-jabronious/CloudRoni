# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-14 16:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0003_league_ended'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('individual', models.CharField(max_length=200)),
                ('team_name', models.CharField(max_length=200)),
                ('total_points', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='season',
            name='first',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first', to='leagues.Winner'),
        ),
        migrations.AddField(
            model_name='season',
            name='league',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.League'),
        ),
        migrations.AddField(
            model_name='season',
            name='second',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second', to='leagues.Winner'),
        ),
        migrations.AddField(
            model_name='season',
            name='thrid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='third', to='leagues.Winner'),
        ),
    ]