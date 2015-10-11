# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('project_name', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='projects')),
            ],
        ),
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('tracker_name', models.CharField(max_length=100)),
                ('goal_name', models.CharField(max_length=100)),
                ('goal_date', models.DateTimeField()),
                ('goal_value', models.IntegerField()),
                ('current_words', models.IntegerField()),
                ('tracker_project', models.ForeignKey(to='wordtracker.Project', related_name='trackers')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WordCount',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('words_datetime', models.DateTimeField()),
                ('words', models.IntegerField()),
                ('tracker', models.ForeignKey(to='wordtracker.Tracker', related_name='wordcounts')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='wordcounts')),
            ],
        ),
    ]
