# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20151016_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='sport_choose',
            field=models.CharField(max_length=60, choices=[('American Football', 'American Football'), ('Badminton', 'Badminton'), ('Futsal', 'Futsal'), ('Hokej na lodzie', 'Hokej na lodzie'), ('Koszykówka', 'Koszykówka'), ('Kręgle', 'Kręgle'), ('Paintball', 'Paintball'), ('Piłka nożna', 'Piłka nożna'), ('Piłka ręczna', 'Piłka ręczna'), ('Rugdy', 'Rugdy'), ('Siatkówka', 'Siatkówka'), ('Siatkówka plażowa', 'Siatkówka plażowa'), ('Szachy', 'Szachy'), ('Tenis', 'Tenis')], blank=True),
            preserve_default=True,
        ),
    ]
