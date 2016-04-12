# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_remove_notifications_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='action_object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notifications',
            name='target_object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
