# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-18 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor_section', '0002_auto_20170918_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='sensor',
            field=models.CharField(default='activity', max_length=20),
        ),
    ]