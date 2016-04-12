# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0005_auto_20151230_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notifications',
            name='unread',
        ),
    ]
