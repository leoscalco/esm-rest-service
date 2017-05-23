from __future__ import unicode_literals

from django.db import models
from trigger_section.models import EventTrigger
from sensor_section.models import Sensor
from intervation_section.models import EmptyIntervention, TaskIntervention, MediaIntervention, QuestionIntervention
from result_section.models import MediaResult, TaskResult, QuestionResult, SensorResult

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    group = models.CharField(max_length=100)

    sensors = models.ManyToManyField(Sensor)

    class Meta:
        abstract = True

class ActiveEvent(Event):
    type = models.CharField(max_length=50, default="active")
    # pensar uma melhor forma de resolver essa situacao (import de classe abstrata)
    empty_interventions = models.ManyToManyField(EmptyIntervention, blank=True)
    task_interventions = models.ManyToManyField(TaskIntervention, blank=True)
    question_interventions = models.ManyToManyField(QuestionIntervention, blank=True)
    media_interventions = models.ManyToManyField(MediaIntervention, blank=True)

    triggers = models.ManyToManyField(EventTrigger)

    media_results = models.ManyToManyField(MediaResult, blank=True)
    task_results = models.ManyToManyField(TaskResult, blank=True)
    question_results = models.ManyToManyField(QuestionResult, blank=True)
    sensor_results = models.ManyToManyField(SensorResult, blank=True)


class PassiveEvent(Event):
    type = models.CharField(max_length=50, default="passive")


    # list de results
    # aqui

