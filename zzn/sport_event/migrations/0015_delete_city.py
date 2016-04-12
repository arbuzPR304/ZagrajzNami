# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport_event', '0014_events_players'),
    ]

    operations = [
        migrations.DeleteModel(
            name='City',
        ),
    ]
