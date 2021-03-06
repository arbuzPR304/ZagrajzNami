# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sport_event', '0013_auto_20160410_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='players',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='players'),
            preserve_default=True,
        ),
    ]
