from __future__ import unicode_literals

from django.db import models
from trigger_section.models import EventTrigger
from sensor_section.models import Sensor
from intervation_section.models import EmptyIntervention, TaskIntervention, MediaIntervention, QuestionIntervention, Intervention
# from result_section.models import *

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, default="", blank=True)
    group = models.CharField(max_length=100, blank=True, default="")
    type = models.CharField(max_length=50, default="active")

    sensors = models.ManyToManyField(Sensor, blank=True)

class ActiveEvent(Event):
    # pensar uma melhor forma de resolver essa situacao (import de classe abstrata)
    interventions = models.ManyToManyField(Intervention, blank=True)

    triggers = models.ManyToManyField(EventTrigger, blank=True)

    # results = models.ManyToManyField(Result, blank=True)


class PassiveEvent(Event):
    # type = models.CharField(max_length=50, default="passive")

    def __init__(self, *args, **kwargs):
        kwargs['type'] = "passive"
        super(PassiveEvent, self).__init__(*args, **kwargs)

    # list de results
    # aqui

