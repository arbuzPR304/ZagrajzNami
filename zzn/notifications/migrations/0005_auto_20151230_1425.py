# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_auto_20151230_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='read',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='notifications',
            name='unread',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
