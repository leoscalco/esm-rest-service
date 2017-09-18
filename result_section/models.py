from __future__ import unicode_literals

from django.db import models
from user_section.models import Participant
from intervation_section.models import MediaIntervention, QuestionIntervention, TaskIntervention
from sensor_section.models import Sensor

# Create your models here.

class Result(models.Model):
    started = models.CharField(max_length=50, blank=True)
    ended = models.CharField(max_length=50, blank=True)

    participant = models.ForeignKey(Participant)

    class Meta:
        abstract = True

class MediaResult(Result):
    media = models.ForeignKey(MediaIntervention, null=True, blank=True)
    type = models.CharField(max_length=50, default="media")
    urlForDataFile = models.URLField(blank=True)

class QuestionResult(Result):
    question = models.ForeignKey(QuestionIntervention)
    type = models.CharField(max_length=50, default="question")
    answer = models.CharField(max_length=100)

class SensorResult(Result):
    sensor = models.ForeignKey(Sensor)
    type = models.CharField(max_length=50, default="sensor")
    urlForDataFile = models.URLField()

class TaskResult(Result):
    task = models.ForeignKey(TaskIntervention)
    type = models.CharField(max_length=50, default="task")
    urlForDataFile = models.URLField()

