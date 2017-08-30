from __future__ import unicode_literals

from django.db import models


class EventTrigger(models.Model):
    # /** type trigger (time, manual, contextual). */
    TIME = "T"
    MANUAL = "M"
    CONTEXTUAL = "C"

    TRIGGER_TYPE = (
        (TIME, "time"),
        (MANUAL, "manual"),
        (CONTEXTUAL, "contextual"),
    )

    trigger_type = models.CharField(
        max_length = 1,
        choices = TRIGGER_TYPE,
        default = TIME
    )

    trigger_condition = models.CharField(max_length=50)
    priority = models.CharField(max_length=20)