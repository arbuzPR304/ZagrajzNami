# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport_event', '0002_auto_20151111_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='players',
        ),
        migrations.RemoveField(
            model_name='events',
            name='zip_code',
        ),
        migrations.AlterField(
            model_name='events',
            name='address',
            field=models.CharField(max_length=120, verbose_name='Miasto', null=True),
            preserve_default=True,
        ),
    ]
