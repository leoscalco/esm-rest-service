from __future__ import unicode_literals

from django.db import models
from trigger_section.models import EventTrigger
from sensor_section.models import Sensor
from intervation_section.models import EmptyIntervention, TaskIntervention, MediaIntervention, QuestionIntervention
from result_section.models import MediaResult, TaskResult, QuestionResult, SensorResult

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300, default="", blank=True)
    group = models.CharField(max_length=100)

    sensors = models.ManyToManyField(Sensor, blank=True)

class ActiveEvent(Event):
    type = models.CharField(max_length=50, default="active")
    # pensar uma melhor forma de resolver essa situacao (import de classe abstrata)
    emptyInterventions = models.ManyToManyField(EmptyIntervention, blank=True)
    taskInterventions = models.ManyToManyField(TaskIntervention, blank=True)
    questionInterventions = models.ManyToManyField(QuestionIntervention, blank=True)
    mediaInterventions = models.ManyToManyField(MediaIntervention, blank=True)

    triggers = models.ManyToManyField(EventTrigger)

    mediaResults = models.ManyToManyField(MediaResult, blank=True)
    taskResults = models.ManyToManyField(TaskResult, blank=True)
    questionResults = models.ManyToManyField(QuestionResult, blank=True)
    sensorResults = models.ManyToManyField(SensorResult, blank=True)


class PassiveEvent(Event):
    type = models.CharField(max_length=50, default="passive")


    # list de results
    # aqui

