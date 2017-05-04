# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tablefor2', '0003_auto_20170416_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_authenticated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
