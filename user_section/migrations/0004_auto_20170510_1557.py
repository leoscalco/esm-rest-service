# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-10 15:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_section', '0003_auto_20170510_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='contacts',
        ),
        migrations.RemoveField(
            model_name='observer',
            name='contacts',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='contacts',
        ),
        migrations.AddField(
            model_name='participant',
            name='observer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Observador', to='user_section.Observer'),
        ),
    ]