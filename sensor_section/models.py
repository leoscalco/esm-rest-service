from __future__ import unicode_literals

from django.db import models

class Sensor(models.Model):
    #   /** Used for capturing sensors during an interval. */
    SENSOR_TYPE_INTERVAL = models.IntegerField(default=0)

    #   /** Used for capturing sensors during a event. */
    SENSOR_TYPE_TASK = models.IntegerField(default=1)

    SENSOR_ACTIVITY = models.CharField(default="activity", max_length=50)
    SENSOR_ACCELEROMETER = models.CharField(default="accelerometer", max_length=50)
    SENSOR_CAMERA = models.CharField(default="camera", max_length=50)
    SENSOR_LIGHT = models.CharField(default="light", max_length=50)
    SENSOR_MICROPHONE = models.CharField(default="microphone", max_length=50)

    # /** Interval or whole event. */
    sensor_type = models.IntegerField(null=False)

    # /** ACITIVTY, LIGHT, AUDIO, ETC. */
    sensor = models.CharField(null=False, max_length=100)

    def __unicode__(self):
        return u'%s' % self.sensor
