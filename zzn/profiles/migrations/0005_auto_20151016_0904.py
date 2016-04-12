# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_sport_choose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sport_choose',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=3, choices=[(1, 'American Football'), (2, 'Badminton'), (3, 'Futsal'), (4, 'Hokej na lodzie'), (5, 'Koszykówka'), (6, 'Kręgle'), (7, 'Paintball'), (8, 'Piłka nożna'), (9, 'Piłka ręczna'), (10, 'Rugdy'), (11, 'Siatkówka'), (12, 'Siatkówka plażowa'), (13, 'Szachy'), (14, 'Tenis')]),
            preserve_default=True,
        ),
    ]
