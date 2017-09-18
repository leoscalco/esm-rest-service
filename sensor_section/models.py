from __future__ import unicode_literals

from django.db import models

class Sensor(models.Model):
    #   /** Used for capturing sensors during an interval. */
    SENSOR_TYPE_INTERVAL = models.IntegerField(default=0)

    #   /** Used for capturing sensors during a event. */
    SENSOR_TYPE_TASK = models.IntegerField(default=1)

    SENSOR_ACTIVITY = "activity"
    SENSOR_ACCELEROMETER = "accelerometer"
    SENSOR_CAMERA = "camera"
    SENSOR_LIGHT = "light"
    SENSOR_MICROPHONE = "microphone"

    # SENSOR_TYPE = (
    #     ("ACT", SENSOR_ACTIVITY),
    #     ("ACC", SENSOR_ACCELEROMETER),
    #     ("CAM", SENSOR_CAMERA),
    #     ("LIG", SENSOR_LIGHT),
    #     ("MIC",SENSOR_MICROPHONE)
    # )

    # /** Interval or whole event. */
    sensorType = models.IntegerField(null=False)

    # /** ACITIVTY, LIGHT, AUDIO, ETC. */
    sensor = models.CharField(max_length=20, default=SENSOR_ACTIVITY)

    def __unicode__(self):
        return u'%s' % self.sensor
