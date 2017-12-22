from __future__ import unicode_literals

from django.db import models

from event_section.models import ActiveEvent, PassiveEvent, Event
from user_section.models import Participant, Observer


class Program(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500, default="", blank=True)
    starts = models.CharField(max_length=50, default="", blank=True)
    ends = models.CharField(max_length=50, default="", blank=True)
    updateDate = models.CharField(max_length=50, default="", blank=True)

    participants = models.ManyToManyField(Participant)
    observers = models.ManyToManyField(Observer)
    events = models.ManyToManyField(Event)
    # passiveEvents = models.ManyToManyField(PassiveEvent)
