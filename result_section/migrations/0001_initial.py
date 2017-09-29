# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-28 20:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('intervation_section', '0001_initial'),
        ('user_section', '0001_initial'),
        ('sensor_section', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started', models.CharField(blank=True, max_length=50)),
                ('ended', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MediaResult',
            fields=[
                ('result_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='result_section.Result')),
                ('type', models.CharField(default='media', max_length=50)),
                ('urlForDataFile', models.URLField(blank=True)),
                ('media', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='intervation_section.MediaIntervention')),
            ],
            bases=('result_section.result',),
        ),
        migrations.CreateModel(
            name='QuestionResult',
            fields=[
                ('result_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='result_section.Result')),
                ('type', models.CharField(default='question', max_length=50)),
                ('answer', models.CharField(max_length=100)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intervation_section.QuestionIntervention')),
            ],
            bases=('result_section.result',),
        ),
        migrations.CreateModel(
            name='SensorResult',
            fields=[
                ('result_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='result_section.Result')),
                ('type', models.CharField(default='sensor', max_length=50)),
                ('urlForDataFile', models.URLField()),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensor_section.Sensor')),
            ],
            bases=('result_section.result',),
        ),
        migrations.CreateModel(
            name='TaskResult',
            fields=[
                ('result_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='result_section.Result')),
                ('type', models.CharField(default='task', max_length=50)),
                ('urlForDataFile', models.URLField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intervation_section.TaskIntervention')),
            ],
            bases=('result_section.result',),
        ),
        migrations.AddField(
            model_name='result',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_section.Participant'),
        ),
    ]
