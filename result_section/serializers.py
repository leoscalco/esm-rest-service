# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from result_section.models import *
from user_section.serializers import ParticipantSerializer
from event_section.serializers import EventVerboseSerializer
from intervation_section.serializers import MediaInterventionSerializer, TaskInterventionSerializer, QuestionInterventionSerializer
from sensor_section.serializers import SensorSerializer

class ResultSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResultSession
        fields = ('id', 'started', 'ended',
            'participant', 'event',
            'results'
            )

class ResultsVerboseSerializer(serializers.ModelSerializer):
    # media = MediaInterventionSerializer()
    # participant = ParticipantSerializer()

    class Meta:
        model = Result
        fields = ('id', 'type' ,'started', 'ended')

    def to_representation(self, obj):
        """
        Because Results is Polymorphic
        """
        if obj.type == "sensor":
            obj = SensorResult.objects.get(id=obj.id)
            return SensorResultVerboseSerializer(obj, context=self.context).to_representation(obj)
        elif obj.type == "question":
            obj = QuestionResult.objects.get(id=obj.id)
            return QuestionResultVerboseSerializer(obj, context=self.context).to_representation(obj)
        elif obj.type == "task":
            obj = TaskResult.objects.get(id=obj.id)
            return TaskResultVerboseSerializer(obj, context=self.context).to_representation(obj)
        elif obj.type == "media":
            obj = MediaResult.objects.get(id=obj.id)
            return MediaResultVerboseSerializer(context=self.context).to_representation(obj)
        else:
            return super(ResultsSerializer, self).to_representation(obj)

class ResultsSerializer(serializers.ModelSerializer):
    # media = MediaInterventionSerializer()
    # participant = ParticipantSerializer()

    class Meta:
        model = Result
        fields = ('id', 'type' ,'started', 'ended')

    def to_representation(self, obj):
        """
        Because Results is Polymorphic
        """
        if obj.type == "sensor":
            obj = SensorResult.objects.get(id=obj.id)
            return SensorResultSerializer(obj, context=self.context).to_representation(obj)
        elif obj.type == "question":
            obj = QuestionResult.objects.get(id=obj.id)
            return QuestionResultSerializer(obj, context=self.context).to_representation(obj)
        elif obj.type == "task":
            obj = TaskResult.objects.get(id=obj.id)
            return TaskResultSerializer(obj, context=self.context).to_representation(obj)
        elif obj.type == "media":
            obj = MediaResult.objects.get(id=obj.id)
            return MediaResultSerializer(context=self.context).to_representation(obj)
        else:
            return super(ResultsSerializer, self).to_representation(obj)

class ResultSessionVerboseSerializer(serializers.ModelSerializer):

    participant = ParticipantSerializer()
    event = EventVerboseSerializer()
    results = ResultsVerboseSerializer(many=True)

    class Meta:
        model = ResultSession
        fields = ('id', 'started', 'ended',
            'participant', 'event',
            'results'
            )

class MediaResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = MediaResult
        fields = ('id', 'type' ,'started', 'ended',
            'urlForDataFile', 'media')

class MediaResultVerboseSerializer(serializers.ModelSerializer):
    # just id without, dict with
    # participant = ParticipantSerializer()
    media = MediaInterventionSerializer()

    class Meta:
        model = MediaResult
        fields = ('id', 'type' ,'started', 'ended',
            'urlForDataFile', 'media')

class SensorResultSerializer(serializers.ModelSerializer):
    # just id without, dict with
    # participant = ParticipantSerializer(read_only=True)
    # media = MediaInterventionSerializer()

    class Meta:
        model = SensorResult
        fields = ('id', 'type' ,'started', 'ended',
            'urlForDataFile', 'sensor')

class SensorResultVerboseSerializer(serializers.ModelSerializer):
    # just id without, dict with
    # participant = ParticipantSerializer()
    sensor = SensorSerializer()

    class Meta:
        model = SensorResult
        fields = ('id', 'type' ,'started', 'ended',
            'urlForDataFile', 'sensor')

class TaskResultSerializer(serializers.ModelSerializer):
    # just id without, dict with
    # participant = ParticipantSerializer(read_only=True)
    # media = MediaInterventionSerializer()

    class Meta:
        model = TaskResult
        fields = ('id', 'type' ,'started', 'ended',
            'urlForDataFile', 'task')

class TaskResultVerboseSerializer(serializers.ModelSerializer):
    # just id without, dict with
    # participant = ParticipantSerializer()
    task = TaskInterventionSerializer()

    class Meta:
        model = TaskResult
        fields = ('id', 'type' ,'started', 'ended',
            'urlForDataFile', 'task')

class QuestionResultSerializer(serializers.ModelSerializer):
    # just id without, dict with
    # participant = ParticipantSerializer(read_only=True)
    # media = MediaInterventionSerializer()

    class Meta:
        model = QuestionResult
        fields = ('id', 'type' ,'started', 'ended',
            'answer', 'question')

class QuestionResultVerboseSerializer(serializers.ModelSerializer):
    # just id without, dict with
    # participant = ParticipantSerializer()
    # self.question_id = serializers.IntegerField(source='question.id')

    question = QuestionInterventionSerializer()

    class Meta:
        model = QuestionResult
        fields = ('id', 'type' ,'started', 'ended',
            'answer', 'question')

    def create(self, validated_data):
        intervention = validated_data.pop('question')
        question_id = self.data["question"]["id"]

        result = QuestionResult.objects.create(
            started=self.data["started"],
            ended=self.data["ended"],
            type=self.data["type"],
            question=QuestionIntervention.objects.get(id=question_id),
            answer=self.data["answer"]
            )

        return result

