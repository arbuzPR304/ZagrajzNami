# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport_event', '0009_auto_20151228_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='duration',
            field=models.TimeField(verbose_name='Czas trwania', null=True),
            preserve_default=True,
        ),
    ]
