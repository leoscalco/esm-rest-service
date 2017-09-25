# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from event_section.models import ActiveEvent
from result_section.serializers import *
from trigger_section.serializers import EventTriggerSerializer;
from sensor_section.serializers import SensorSerializer
from intervation_section.serializers import *

# PASSANDO SOMENTE O ID

class ActiveEventWriteSerializer(serializers.ModelSerializer):
    # just id without, dict with
    # participant = ParticipantSerializer(read_only=True)
    # media = MediaInterventionSerializer()

    class Meta:
        model = ActiveEvent
        fields = ('id', 'type', 'title' , 'description',
           'mediaResults', 'taskResults', 'questionResults', 'sensorResults',
           'triggers', 'sensors',
           'emptyInterventions', 'taskInterventions', 'questionInterventions', 'mediaInterventions' )

class ActiveEventReadSerializer(serializers.ModelSerializer):
    # just id without, dict with
    mediaResults = MediaResultReadSerializer(many=True)
    taskResults = TaskResultReadSerializer(many=True)
    questionResults = QuestionResultReadSerializer(many=True)
    sensorResults = SensorResultReadSerializer(many=True)

    triggers = EventTriggerSerializer(many=True)
    sensors = SensorSerializer(many=True)

    emptyInterventions = EmptyInterventionSerializer(many=True)
    taskInterventions = TaskInterventionSerializer(many=True)
    questionInterventions = QuestionInterventionSerializer(many=True)
    mediaInterventions = MediaInterventionSerializer(many=True)

    class Meta:
        model = ActiveEvent
        fields = ('id', 'type', 'title' , 'description',
           'mediaResults', 'taskResults', 'questionResults', 'sensorResults',
           'triggers', 'sensors',
           'emptyInterventions', 'taskInterventions', 'questionInterventions', 'mediaInterventions' )

