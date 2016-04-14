# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='organized_match',
            field=models.IntegerField(default=0, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='played_match',
            field=models.IntegerField(default=0, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(default='Opole', blank=True, null=True, max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=profiles.models.upload_location),
            preserve_default=True,
        ),
    ]
