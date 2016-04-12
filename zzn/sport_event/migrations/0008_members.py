# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sport_event', '0007_auto_20151112_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('event', models.OneToOneField(serialize=False, to='sport_event.Events', primary_key=True)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
