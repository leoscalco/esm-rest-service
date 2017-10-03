# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from result_section.models import *
from user_section.serializers import ParticipantSerializer
from intervation_section.serializers import MediaInterventionSerializer, TaskInterventionSerializer, QuestionInterventionSerializer
from sensor_section.serializers import SensorSerializer

class ResultsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = ('id', 'type' ,'started', 'ended', 'participant'
        )

    def to_representation(self, obj):
        """
        Because Results is Polymorphic
        """
        if obj.type == "sensor":
            obj = SensorResult.objects.get(id=obj.id)
            return SensorResultReadSerializer(obj, context=self.context).to_representation(obj)
        elif obj.type == "question":
            obj = QuestionResult.objects.get(id=obj.id)
            return QuestionResultReadSerializer(obj, context=self.context).to_representation(obj)
        elif obj.type == "task":
            obj = TaskResult.objects.get(id=obj.id)
            return TaskResultReadSerializer(obj, context=self.context).to_representation(obj)
        elif obj.type == "media":
            obj = MediaResult.objects.get(id=obj.id)
            return MediaResultReadSerializer(context=self.context).to_representation(obj)
        else:
            return super(ResultsSerializer, self).to_representation(obj)


class MediaResultWriteSerializer(serializers.ModelSerializer):
    # just id without, dict with
    # participant = ParticipantSerializer(read_only=True)
    # media = MediaInterventionSerializer()

    class Meta:
        model = MediaResult
        fields = ('id', 'type' ,'started', 'ended',
            'urlForDataFile', 'media', 'participant')

class MediaResultReadSerializer(serializers.ModelSerializer):
    # just id without, dict with
    participant = ParticipantSerializer()
    media = MediaInterventionSerializer()

    class Meta:
        model = MediaResult
        fields = ('id', 'type' ,'started', 'ended',
            'urlForDataFile', 'media', 'participant')

class SensorResultWriteSerializer(serializers.ModelSerializer):
    # just id without, dict with
    # participant = ParticipantSerializer(read_only=True)
    # media = MediaInterventionSerializer()

    class Meta:
        model = SensorResult
        fields = ('id', 'type' ,'started', 'ended',
            'urlForDataFile', 'sensor', 'participant')

class SensorResultReadSerializer(serializers.ModelSerializer):
    # just id without, dict with
    participant = ParticipantSerializer()
    sensor = SensorSerializer()

    class Meta:
        model = SensorResult
        fields = ('id', 'type' ,'started', 'ended',
            'urlForDataFile', 'sensor', 'participant')

class TaskResultWriteSerializer(serializers.ModelSerializer):
    # just id without, dict with
    # participant = ParticipantSerializer(read_only=True)
    # media = MediaInterventionSerializer()

    class Meta:
        model = TaskResult
        fields = ('id', 'type' ,'started', 'ended',
            'urlForDataFile', 'task', 'participant')

class TaskResultReadSerializer(serializers.ModelSerializer):
    # just id without, dict with
    participant = ParticipantSerializer()
    task = TaskInterventionSerializer()

    class Meta:
        model = TaskResult
        fields = ('id', 'type' ,'started', 'ended',
            'urlForDataFile', 'task', 'participant')

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