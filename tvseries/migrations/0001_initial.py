# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('country', models.CharField(blank=True, default='', max_length=100)),
                ('tvpartners', models.CharField(blank=True, default='', max_length=100)),
                ('language', models.CharField(blank=True, default='', max_length=100)),
                ('summary', models.TextField()),
                ('premiered', models.DateField()),
                ('runtime', models.IntegerField()),
                ('genres', models.CharField(blank=True, default='', max_length=100)),
                ('status', models.BooleanField()),
                ('image_med', models.URLField()),
                ('image_org', models.URLField()),
                ('imdblink', models.URLField()),
                ('raiting', models.FloatField()),
            ],
        ),
    ]