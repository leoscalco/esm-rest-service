from __future__ import unicode_literals

from annoying.fields import JSONField
from django.db import models


# Create your models here.

class MediaPresentation(models.Model):
    # TYPE = (
    #     (IMAGEM, "imagem"),
    #     (AUDIO, "audio"),
    #     (VIDEO, "video"),
    # )

    type = models.CharField(
        max_length=10,
        default="image"
    )

    mediaUrl = models.URLField()


class ComplexCondition(models.Model):
    value = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    condition = models.CharField(max_length=100, blank=True)
    next = models.IntegerField()


class Intervention(models.Model):
    type = models.CharField(max_length=10, default="empty")
    statement = models.CharField(max_length=800)
    medias = models.ManyToManyField(MediaPresentation)
    orderPosition = models.IntegerField()
    first = models.BooleanField(default=False)
    next = models.IntegerField()
    obligatory = models.BooleanField(default=False)


class EmptyIntervention(Intervention):

    def __init__(self, *args, **kwargs):
        kwargs['type'] = "empty"
        super(EmptyIntervention, self).__init__(*args, **kwargs)


class MediaIntervention(Intervention):
    # TYPE = (
    #     (IMAGEM, "image"),
    #     (AUDIO, "audio"),
    #     (VIDEO, "video"),
    # )

    mediaType = models.CharField(
        max_length=10,
        default="image"
    )

    def __init__(self, *args, **kwargs):
        kwargs['type'] = "media"
        super(MediaIntervention, self).__init__(*args, **kwargs)


class QuestionIntervention(Intervention):
    QUESTION_TYPE_OPEN_TEXT = 0
    QUESTION_TYPE_RADIO = 1
    QUESTION_TYPE_CHECKBOX = 2
    QUESTION_TYPE_LIKERT = 3
    QUESTION_TYPE_SEMANTIC_DIFFERENTIAL = 4

    QUESTION_TYPE = (
        (QUESTION_TYPE_OPEN_TEXT, "open_text"),
        (QUESTION_TYPE_RADIO, "radio"),
        (QUESTION_TYPE_CHECKBOX, "checkbox"),
        (QUESTION_TYPE_LIKERT, "likert"),
        (QUESTION_TYPE_SEMANTIC_DIFFERENTIAL, 'semantic_differential'),
    )

    questionType = models.IntegerField(
        choices=QUESTION_TYPE,
        default=0
    )
    conditions = JSONField(blank=True, null=True)
    options = JSONField(blank=True, null=True)
    complexConditions = models.ManyToManyField(ComplexCondition, blank=True)

    def __init__(self, *args, **kwargs):
        kwargs['type'] = "question"
        super(QuestionIntervention, self).__init__(*args, **kwargs)


class TaskIntervention(Intervention):
    appPackage = models.CharField(max_length=50)
    parameters = JSONField(blank=True, null=True)

    def __init__(self, *args, **kwargs):
        kwargs['type'] = "task"
        super(TaskIntervention, self).__init__(*args, **kwargs)
