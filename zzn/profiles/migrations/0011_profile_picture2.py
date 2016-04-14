# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20151210_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='picture2',
            field=models.ImageField(default=0, upload_to=profiles.models.upload_location),
            preserve_default=False,
        ),
    ]
