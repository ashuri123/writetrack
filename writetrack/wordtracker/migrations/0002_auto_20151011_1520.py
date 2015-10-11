# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordtracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='tracker_project',
            field=models.ForeignKey(related_name='trackers', blank=True, to='wordtracker.Project'),
        ),
    ]
