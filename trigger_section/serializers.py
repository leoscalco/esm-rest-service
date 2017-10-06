# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from trigger_section.models import EventTrigger

class EventTriggerSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventTrigger
        # fields = ('id', 'sensor_type', 'sensor')
        fields = ('id', 'triggerType', 'triggerCondition',
            'priority'
        )
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }

    def create(self, validated_data):
        if len(EventTrigger.objects.all()) == 0:
            validated_data['id'] = 1
        else:
            validated_data['id'] = (EventTrigger.objects.all().latest('id').id) + 1

        p = EventTrigger.objects.create(**validated_data)

        return p
