# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-25 01:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SENSOR_TYPE_INTERVAL', models.IntegerField(default=0)),
                ('SENSOR_TYPE_TASK', models.IntegerField(default=1)),
                ('sensorType', models.IntegerField()),
                ('sensor', models.CharField(default='activity', max_length=20)),
            ],
        ),
    ]
