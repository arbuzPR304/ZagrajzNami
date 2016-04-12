# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport_event', '0008_members'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='event',
            field=models.ForeignKey(to='sport_event.Events', blank=True, null=True),
            preserve_default=True,
        ),
    ]
