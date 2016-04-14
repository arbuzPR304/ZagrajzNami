# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20151017_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.FileField(blank=True, upload_to=profiles.models.upload_location, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='sport_choose',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('American Football', 'American Football'), ('Badminton', 'Badminton'), ('Futsal', 'Futsal'), ('Hokej na lodzie', 'Hokej na lodzie'), ('Koszykówka', 'Koszykówka'), ('Kręgle', 'Kręgle'), ('Paintball', 'Paintball'), ('Piłka nożna', 'Piłka nożna'), ('Piłka ręczna', 'Piłka ręczna'), ('Siatkówka', 'Siatkówka'), ('Siatkówka plażowa', 'Siatkówka plażowa'), ('Szachy', 'Szachy'), ('Tenis', 'Tenis')], max_length=500),
            preserve_default=True,
        ),
    ]
