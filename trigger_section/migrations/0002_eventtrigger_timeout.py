# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-22 05:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trigger_section', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventtrigger',
            name='timeOut',
            field=models.IntegerField(default=1800000),
        ),
    ]
