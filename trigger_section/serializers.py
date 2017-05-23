# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from trigger_section.models import EventTrigger

class EventTriggerSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventTrigger
        # fields = ('id', 'sensor_type', 'sensor')
        fields = ('id', 'trigger_type', 'trigger_condition',
            'priority'
        )
