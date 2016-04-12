# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import durationfield.db.models.fields.duration
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sport_event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='address',
            field=models.CharField(null=True, verbose_name='Ulica', max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='events',
            name='date_event',
            field=models.DateTimeField(null=True, verbose_name='Data wydarzenia'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='events',
            name='duration',
            field=durationfield.db.models.fields.duration.DurationField(null=True, verbose_name='Czas trwania'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='events',
            name='max_number_of_player',
            field=models.IntegerField(null=True, verbose_name='Maksymalna liczna graczy'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='events',
            name='number_street',
            field=models.IntegerField(null=True, verbose_name='Numer ulicy'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='events',
            name='organizer',
            field=models.ForeignKey(verbose_name='Organizator', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='events',
            name='players',
            field=models.ManyToManyField(verbose_name='Gracze', to='profiles.Profile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='events',
            name='profession_choose',
            field=models.ForeignKey(verbose_name='Dyscyplina', to='sport_event.Disciplines'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='events',
            name='rules',
            field=models.CharField(verbose_name='Zasady', blank=True, max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='events',
            name='title',
            field=models.CharField(null=True, verbose_name='Nazwa wydarzenia', max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='events',
            name='zip_code',
            field=models.CharField(null=True, verbose_name='Kod pocztowy', max_length=5),
            preserve_default=True,
        ),
    ]
