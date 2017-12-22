from __future__ import unicode_literals

from django.db import models

from event_section.models import Event
from intervention_section.models import MediaIntervention, QuestionIntervention, TaskIntervention, EmptyIntervention
from sensor_section.models import Sensor
from user_section.models import Participant


# Create your models here.

class Result(models.Model):
    started = models.CharField(max_length=50, blank=True)
    ended = models.CharField(max_length=50, blank=True)
    type = models.CharField(max_length=10, default="question")
    # participant = models.ForeignKey(Participant)


class ResultSession(models.Model):
    started = models.CharField(max_length=50, blank=True)
    ended = models.CharField(max_length=50, blank=True)
    participant = models.ForeignKey(Participant)
    event = models.ForeignKey(Event)
    results = models.ManyToManyField(Result)


class MediaResult(Result):
    media = models.ForeignKey(MediaIntervention, null=True, blank=True)
    # type = models.CharField(max_length=50, default="media")
    urlForDataFile = models.URLField(blank=True)

    def __init__(self, *args, **kwargs):
        kwargs['type'] = "media"
        super(MediaResult, self).__init__(*args, **kwargs)


class QuestionResult(Result):
    question = models.ForeignKey(QuestionIntervention)
    # type = models.CharField(max_length=50, default="question")
    answer = models.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        kwargs['type'] = "question"
        super(QuestionResult, self).__init__(*args, **kwargs)


class SensorResult(Result):
    sensor = models.ForeignKey(Sensor)
    # type = models.CharField(max_length=50, default="sensor")
    urlForDataFile = models.URLField()

    def __init__(self, *args, **kwargs):
        kwargs['type'] = "sensor"
        super(SensorResult, self).__init__(*args, **kwargs)


class TaskResult(Result):
    task = models.ForeignKey(TaskIntervention)
    # type = models.CharField(max_length=50, default="task")
    urlForDataFile = models.URLField()

    def __init__(self, *args, **kwargs):
        kwargs['type'] = "task"
        super(TaskResult, self).__init__(*args, **kwargs)


class EmptyResult(Result):
    empty = models.ForeignKey(EmptyIntervention)

    # type = models.CharField(max_length=50, default="task")
    # urlForDataFile = models.URLField()

    def __init__(self, *args, **kwargs):
        kwargs['type'] = "empty"
        super(EmptyResult, self).__init__(*args, **kwargs)
