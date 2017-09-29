# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-28 20:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(default='', max_length=254, unique=True)),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='user_section.Person')),
                ('password', models.CharField(max_length=20)),
            ],
            bases=('user_section.person',),
        ),
        migrations.CreateModel(
            name='Observer',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='user_section.Person')),
                ('role', models.CharField(max_length=50)),
            ],
            bases=('user_section.person',),
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='user_section.Person')),
                ('observerResponsible', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='user_section.Observer')),
            ],
            bases=('user_section.person',),
        ),
    ]
