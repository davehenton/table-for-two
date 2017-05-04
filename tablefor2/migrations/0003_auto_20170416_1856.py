# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tablefor2', '0002_auto_20170416_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='matched_email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='availability',
            name='matched_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
