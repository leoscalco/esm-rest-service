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
           'media_results', 'task_results', 'question_results', 'sensor_results',
           'triggers', 'sensors',
           'empty_interventions', 'task_interventions', 'question_interventions', 'media_interventions' )

class ActiveEventReadSerializer(serializers.ModelSerializer):
    # just id without, dict with
    media_results = MediaResultReadSerializer(many=True)
    task_results = TaskResultReadSerializer(many=True)
    question_results = QuestionResultReadSerializer(many=True)
    sensor_results = SensorResultReadSerializer(many=True)

    triggers = EventTriggerSerializer(many=True);
    sensors = SensorSerializer(many=True)

    empty_interventions = EmptyInterventionSerializer(many=True)
    task_interventions = TaskInterventionSerializer(many=True)
    question_interventions = QuestionInterventionSerializer(many=True)
    media_interventions = MediaInterventionSerializer(many=True)

    class Meta:
        model = ActiveEvent
        fields = ('id', 'type', 'title' , 'description',
           'media_results', 'task_results', 'question_results', 'sensor_results',
           'triggers', 'sensors',
           'empty_interventions', 'task_interventions', 'question_interventions', 'media_interventions' )

