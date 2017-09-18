# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(default='', unique=True)
    # contacts = models.ManyToManyField("self", related_name='contatos', blank=True)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def __unicode__(self):
        return u'%s' % self.name

class Observer(Person):
    role = models.CharField(max_length=50)

class Participant(Person):

    observerResponsible = models.ForeignKey(Observer, related_name="contacts", on_delete=models.CASCADE, default=1)

    def __unicode__(self):
        return u'%s' % self.name

class Admin(Person):
    password = models.CharField(max_length=20)

