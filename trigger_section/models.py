from __future__ import unicode_literals

from django.db import models


class EventTrigger(models.Model):
    # /** type trigger (time, manual, contextual). */
    # TIME = "T"
    # MANUAL = "M"
    # CONTEXTUAL = "C"

    # TRIGGER_TYPE = (
    #     (TIME, "time"),
    #     (MANUAL, "manual"),
    #     (CONTEXTUAL, "contextual"),
    # )

    triggerType = models.CharField(
        max_length = 10,
        default = "time"
    )

    triggerCondition = models.CharField(max_length=50)
    priority = models.CharField(max_length=20)
