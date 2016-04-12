# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20151016_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about_player',
            field=models.CharField(null=True, max_length=5000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='sport_choose',
            field=multiselectfield.db.fields.MultiSelectField(max_length=60, blank=True, choices=[('American Football', 'American Football'), ('Badminton', 'Badminton'), ('Futsal', 'Futsal'), ('Hokej na lodzie', 'Hokej na lodzie'), ('Koszykówka', 'Koszykówka'), ('Kręgle', 'Kręgle'), ('Paintball', 'Paintball'), ('Piłka nożna', 'Piłka nożna'), ('Piłka ręczna', 'Piłka ręczna'), ('Rugdy', 'Rugdy'), ('Siatkówka', 'Siatkówka'), ('Siatkówka plażowa', 'Siatkówka plażowa'), ('Szachy', 'Szachy'), ('Tenis', 'Tenis')]),
            preserve_default=True,
        ),
    ]
