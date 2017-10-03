# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-03 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventTrigger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('triggerType', models.CharField(default='time', max_length=10)),
                ('triggerCondition', models.CharField(max_length=50)),
                ('priority', models.CharField(max_length=20)),
            ],
        ),
    ]
