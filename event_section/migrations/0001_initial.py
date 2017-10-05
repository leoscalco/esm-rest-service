# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-05 13:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sensor_section', '0001_initial'),
        ('intervation_section', '0001_initial'),
        ('trigger_section', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, default='', max_length=300)),
                ('type', models.CharField(default='active', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ActiveEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='event_section.Event')),
                ('interventions', models.ManyToManyField(blank=True, to='intervation_section.Intervention')),
                ('triggers', models.ManyToManyField(to='trigger_section.EventTrigger')),
            ],
            bases=('event_section.event',),
        ),
        migrations.CreateModel(
            name='PassiveEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='event_section.Event')),
            ],
            bases=('event_section.event',),
        ),
        migrations.AddField(
            model_name='event',
            name='sensors',
            field=models.ManyToManyField(blank=True, to='sensor_section.Sensor'),
        ),
    ]
