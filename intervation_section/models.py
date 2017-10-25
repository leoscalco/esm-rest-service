from __future__ import unicode_literals

from django.db import models
from annoying.fields import JSONField

# Create your models here.

class MediaPresentation(models.Model):
    # IMAGEM = "I"
    # AUDIO = "A"
    # VIDEO = "V"

    # TYPE = (
    #     (IMAGEM, "imagem"),
    #     (AUDIO, "audio"),
    #     (VIDEO, "video"),
    # )

    type = models.CharField(
        max_length = 10,
        default = "image"
    )

    mediaUrl = models.URLField()

class ComplexCondition(models.Model):
    value = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    condition = models.CharField(max_length=100)
    next = models.IntegerField()

class Intervention(models.Model):
    type = models.CharField(max_length=10, default="empty")
    statement = models.CharField(max_length=100)
    medias = models.ManyToManyField(MediaPresentation)
    orderPosition = models.IntegerField()
    first = models.BooleanField(default=False)
    next = models.IntegerField()
    obligatory = models.BooleanField(default=False)

class EmptyIntervention(Intervention):
    # type = models.CharField(max_length=10, default="empty")

    def __init__(self, *args, **kwargs):
        kwargs['type'] = "empty"
        super(EmptyIntervention, self).__init__(*args, **kwargs)

class MediaIntervention(Intervention):

    # IMAGEM = "I"
    # AUDIO = "A"
    # VIDEO = "V"

    # TYPE = (
    #     (IMAGEM, "image"),
    #     (AUDIO, "audio"),
    #     (VIDEO, "video"),
    # )

    # type = models.CharField(max_length=10, default="media")
    mediaType = models.CharField(
        max_length = 10,
        default = "image"
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

    # type = models.CharField(max_length=10, default="question")
    questionType = models.IntegerField(
        choices=QUESTION_TYPE,
        default=0
    )
    conditions = JSONField(blank=True, null=True)
    options = JSONField(blank=True, null=True)
    complexConditions = models.ManyToManyField(ComplexCondition)

    def __init__(self, *args, **kwargs):
        kwargs['type'] = "question"
        super(QuestionIntervention, self).__init__(*args, **kwargs)

# class MAP_conditions(models.Model):
#     questionIntervention = models.ForeignKey(QuestionIntervention, related_name="conditions")

#     # key is the answer value
#     answer = models.CharField(max_length=300)
#     # question number to jump to.
#     value = models.IntegerField()

# class ARRAY_option(models.Model):
#     questionIntervention = models.ForeignKey(QuestionIntervention, related_name="options")

#     option = models.CharField(max_length=100)

class TaskIntervention(Intervention):
    # type = models.CharField(max_length=10, default="task")
    appPackage = models.CharField(max_length=50)

    def __init__(self, *args, **kwargs):
        kwargs['type'] = "task"
        super(TaskIntervention, self).__init__(*args, **kwargs)