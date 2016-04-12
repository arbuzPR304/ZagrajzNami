# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='action_content_type',
            field=models.ForeignKey(to='contenttypes.ContentType', null=True, blank=True, related_name='notify_action'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='notifications',
            name='action_object_id',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notifications',
            name='sender_content_type',
            field=models.ForeignKey(to='contenttypes.ContentType', default=0, related_name='nofity_sender'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notifications',
            name='sender_object_id',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notifications',
            name='target_content_type',
            field=models.ForeignKey(to='contenttypes.ContentType', null=True, blank=True, related_name='notify_target'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='notifications',
            name='target_object_id',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notifications',
            name='verb',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
