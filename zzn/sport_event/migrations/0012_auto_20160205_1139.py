# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport_event', '0011_auto_20160205_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='city',
            field=models.CharField(null=True, max_length=120, verbose_name='Miasto', default='Opole'),
            preserve_default=True,
        ),
    ]
