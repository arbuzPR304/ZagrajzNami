# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport_event', '0010_auto_20160205_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('city', models.CharField(max_length=120, null=True, verbose_name='Miasto')),
            ],
            options={
                'ordering': ['-city'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='events',
            name='city',
            field=models.ForeignKey(null=True, verbose_name='Miasto', to='sport_event.City'),
            preserve_default=True,
        ),
    ]
