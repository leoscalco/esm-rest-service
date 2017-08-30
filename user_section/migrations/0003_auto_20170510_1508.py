# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-10 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_section', '0002_person_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(default='', max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('contacts', models.ManyToManyField(blank=True, related_name='_admin_contacts_+', to='user_section.Admin')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.CreateModel(
            name='Observer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(default='', max_length=254)),
                ('role', models.CharField(max_length=50)),
                ('contacts', models.ManyToManyField(blank=True, related_name='_observer_contacts_+', to='user_section.Observer')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(default='', max_length=254)),
                ('contacts', models.ManyToManyField(blank=True, related_name='_participant_contacts_+', to='user_section.Participant')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.RemoveField(
            model_name='person',
            name='contacts',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]