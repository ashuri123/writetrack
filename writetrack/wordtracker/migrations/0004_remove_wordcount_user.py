# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordtracker', '0003_auto_20151011_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wordcount',
            name='user',
        ),
    ]
