# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sport_event.models
import datetime
from django.conf import settings
import durationfield.db.models.fields.duration


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0009_auto_20151106_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplines',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=120, null=True, blank=True)),
                ('picture', models.ImageField(upload_to=sport_event.models.upload_loaction, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=120, null=True)),
                ('number_street', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=120, null=True)),
                ('zip_code', models.CharField(max_length=5, null=True)),
                ('date_event', models.DateTimeField(null=True)),
                ('duration', durationfield.db.models.fields.duration.DurationField(null=True)),
                ('max_number_of_player', models.IntegerField(null=True)),
                ('rules', models.CharField(max_length=500, blank=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, auto_now_add=True)),
                ('organizer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('players', models.ManyToManyField(to='profiles.Profile')),
                ('profession_choose', models.ForeignKey(to='sport_event.Disciplines')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
