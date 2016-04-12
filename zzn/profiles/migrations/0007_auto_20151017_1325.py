# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20151016_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about_player',
            field=models.CharField(blank=True, max_length=5000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='sport_choose',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('American Football', 'American Football'), ('Badminton', 'Badminton'), ('Futsal', 'Futsal'), ('Hokej na lodzie', 'Hokej na lodzie'), ('Koszykówka', 'Koszykówka'), ('Kręgle', 'Kręgle'), ('Paintball', 'Paintball'), ('Piłka nożna', 'Piłka nożna'), ('Piłka ręczna', 'Piłka ręczna'), ('Siatkówka', 'Siatkówka'), ('Siatkówka plażowa', 'Siatkówka plażowa'), ('Szachy', 'Szachy'), ('Tenis', 'Tenis')], max_length=60),
            preserve_default=True,
        ),
    ]
