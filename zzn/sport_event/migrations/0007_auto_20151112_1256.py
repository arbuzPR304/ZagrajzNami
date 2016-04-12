# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport_event', '0006_auto_20151112_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='time_event',
            field=models.TimeField(null=True, verbose_name='Czas wydarzenia'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='events',
            name='date_event',
            field=models.DateField(null=True, verbose_name='Data wydarzenia'),
            preserve_default=True,
        ),
    ]
