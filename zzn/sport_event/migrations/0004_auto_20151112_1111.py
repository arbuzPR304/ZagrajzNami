# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport_event', '0003_auto_20151111_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='city',
            field=models.CharField(verbose_name='Miasto', null=True, max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='events',
            name='address',
            field=models.CharField(verbose_name='Ulica', null=True, max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='events',
            name='max_number_of_player',
            field=models.PositiveSmallIntegerField(verbose_name='Maksymalna liczna graczy', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='events',
            name='number_street',
            field=models.PositiveSmallIntegerField(verbose_name='Numer', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='events',
            name='title',
            field=models.CharField(verbose_name='Nazwa', null=True, max_length=120),
            preserve_default=True,
        ),
    ]
