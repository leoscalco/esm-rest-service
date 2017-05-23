# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from result_section.models import *
from user_section.serializers import ParticipantSerializer
from intervation_section.serializers import MediaInterventionSerializer, TaskInterventionSerializer, QuestionInterventionSerializer
from sensor_section.serializers import SensorSerializer

class MediaResultWriteSerializer(serializers.ModelSerializer):
    # just id without, dict with
    # participant = ParticipantSerializer(read_only=True)
    # media = MediaInterventionSerializer()

    class Meta:
        model = MediaResult
        fields = ('id', 'type' ,'started', 'ended',
            'url_for_data_file', 'media', 'participant')

class MediaResultReadSerializer(serializers.ModelSerializer):
    # just id without, dict with
    participant = ParticipantSerializer()
    media = MediaInterventionSerializer()

    class Meta:
        model = MediaResult
        fields = ('id', 'type' ,'started', 'ended',
            'url_for_data_file', 'media', 'participant')

class SensorResultWriteSerializer(serializers.ModelSerializer):
    # just id without, dict with
    # participant = ParticipantSerializer(read_only=True)
    # media = MediaInterventionSerializer()

    class Meta:
        model = SensorResult
        fields = ('id', 'type' ,'started', 'ended',
            'url_for_data_file', 'sensor', 'participant')

class SensorResultReadSerializer(serializers.ModelSerializer):
    # just id without, dict with
    participant = ParticipantSerializer()
    sensor = SensorSerializer()

    class Meta:
        model = SensorResult
        fields = ('id', 'type' ,'started', 'ended',
            'url_for_data_file', 'sensor', 'participant')

class TaskResultWriteSerializer(serializers.ModelSerializer):
    # just id without, dict with
    # participant = ParticipantSerializer(read_only=True)
    # media = MediaInterventionSerializer()

    class Meta:
        model = TaskResult
        fields = ('id', 'type' ,'started', 'ended',
            'url_for_data_file', 'task', 'participant')

class TaskResultReadSerializer(serializers.ModelSerializer):
    # just id without, dict with
    participant = ParticipantSerializer()
    task = TaskInterventionSerializer()

    class Meta:
        model = TaskResult
        fields = ('id', 'type' ,'started', 'ended',
            'url_for_data_file', 'task', 'participant')

class QuestionResultWriteSerializer(serializers.ModelSerializer):
    # just id without, dict with
    # participant = ParticipantSerializer(read_only=True)
    # media = MediaInterventionSerializer()

    class Meta:
        model = QuestionResult
        fields = ('id', 'type' ,'started', 'ended',
            'answer', 'question', 'participant')

class QuestionResultReadSerializer(serializers.ModelSerializer):
    # just id without, dict with
    participant = ParticipantSerializer()
    question = QuestionInterventionSerializer()

    class Meta:
        model = QuestionResult
        fields = ('id', 'type' ,'started', 'ended',
            'answer', 'question', 'participant')