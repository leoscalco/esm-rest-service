from __future__ import unicode_literals

from django.db import models
from user_section.models import Participant, Observer
from event_section.models import ActiveEvent, PassiveEvent

class Program(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    starts = models.CharField(max_length=50)
    ends = models.CharField(max_length=50)
    update_date = models.CharField(max_length=50)

    participants = models.ManyToManyField(Participant)
    observers = models.ManyToManyField(Observer)
    active_events = models.ManyToManyField(ActiveEvent)
    passive_events = models.ManyToManyField(PassiveEvent)
