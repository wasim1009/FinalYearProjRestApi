# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-04 20:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('course', models.CharField(blank=True, default='', max_length=100)),
                ('profession', models.CharField(blank=True, default='', max_length=100)),
                ('module', models.CharField(blank=True, default='', max_length=100)),
                ('description', models.CharField(blank=True, default='', max_length=900)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(blank=True, default='', max_length=100)),
                ('floor_level', models.IntegerField(blank=True, default=0)),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='app.Lecturer')),
            ],
        ),
    ]
