# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-18 17:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('intervation_section', '0001_initial'),
        ('sensor_section', '0001_initial'),
        ('trigger_section', '0001_initial'),
        ('result_section', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('group', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ActiveEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='event_section.Event')),
                ('type', models.CharField(default='active', max_length=50)),
                ('emptyInterventions', models.ManyToManyField(blank=True, to='intervation_section.EmptyIntervention')),
                ('mediaInterventions', models.ManyToManyField(blank=True, to='intervation_section.MediaIntervention')),
                ('mediaResults', models.ManyToManyField(blank=True, to='result_section.MediaResult')),
                ('questionInterventions', models.ManyToManyField(blank=True, to='intervation_section.QuestionIntervention')),
                ('questionResults', models.ManyToManyField(blank=True, to='result_section.QuestionResult')),
                ('sensorResults', models.ManyToManyField(blank=True, to='result_section.SensorResult')),
                ('taskInterventions', models.ManyToManyField(blank=True, to='intervation_section.TaskIntervention')),
                ('taskResults', models.ManyToManyField(blank=True, to='result_section.TaskResult')),
                ('triggers', models.ManyToManyField(to='trigger_section.EventTrigger')),
            ],
            bases=('event_section.event',),
        ),
        migrations.CreateModel(
            name='PassiveEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='event_section.Event')),
                ('type', models.CharField(default='passive', max_length=50)),
            ],
            bases=('event_section.event',),
        ),
        migrations.AddField(
            model_name='event',
            name='sensors',
            field=models.ManyToManyField(to='sensor_section.Sensor'),
        ),
    ]
