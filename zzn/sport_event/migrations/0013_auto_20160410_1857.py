# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport_event', '0012_auto_20160205_1139'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='events',
            options={'ordering': ['date_event']},
        ),
        migrations.AddField(
            model_name='events',
            name='latlong',
            field=models.CharField(null=True, verbose_name='Dlugosc, szerokosc', max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='events',
            name='city',
            field=models.CharField(null=True, verbose_name='Miasto', max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='events',
            name='rules',
            field=models.CharField(verbose_name='Od organizatora', max_length=500, blank=True),
            preserve_default=True,
        ),
    ]
