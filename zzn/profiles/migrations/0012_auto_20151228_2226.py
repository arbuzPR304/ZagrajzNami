# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_profile_picture2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='picture2',
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.FileField(upload_to=profiles.models.upload_location),
            preserve_default=True,
        ),
    ]
