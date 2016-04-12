# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport_event', '0005_auto_20151112_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='time_event',
        ),
        migrations.AlterField(
            model_name='events',
            name='city',
            field=models.CharField(null=True, default='Opole', max_length=120, verbose_name='Miasto'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='events',
            name='date_event',
            field=models.DateTimeField(null=True, verbose_name='Data i czas wydarzenia'),
            preserve_default=True,
        ),
    ]
