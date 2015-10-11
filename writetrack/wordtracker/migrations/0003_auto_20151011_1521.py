# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordtracker', '0002_auto_20151011_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='tracker_project',
            field=models.ForeignKey(blank=True, null=True, to='wordtracker.Project', related_name='trackers'),
        ),
    ]
