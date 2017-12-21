# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-21 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_section', '0001_initial'),
        ('event_section', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(blank=True, default='', max_length=500)),
                ('starts', models.CharField(blank=True, default='', max_length=50)),
                ('ends', models.CharField(blank=True, default='', max_length=50)),
                ('updateDate', models.CharField(blank=True, default='', max_length=50)),
                ('events', models.ManyToManyField(to='event_section.Event')),
                ('observers', models.ManyToManyField(to='user_section.Observer')),
                ('participants', models.ManyToManyField(to='user_section.Participant')),
            ],
        ),
    ]
