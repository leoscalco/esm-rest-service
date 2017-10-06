# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from result_section.models import *
from event_section.models import *
from user_section.serializers import ParticipantSerializer
from event_section.serializers import EventVerboseSerializer
from intervation_section.serializers import MediaInterventionSerializer, TaskInterventionSerializer, QuestionInterventionSerializer
from sensor_section.serializers import SensorSerializer
from intervation_section.models import *
import json

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

    def to_internal_value(self, obj):
        """
        Because Results is Polymorphic
        """
        if obj['type'] == "sensor":
            # self.fields += ()
            obj = SensorResult.objects.get(id=obj['id'])
            return SensorResultVerboseSerializer(obj, context=self.context).to_representation(obj)
        elif obj['type'] == "question":
            obj = QuestionResult.objects.get(id=obj['id'])
            return QuestionResultVerboseSerializer(obj, context=self.context).to_representation(obj)
        elif obj['type'] == "task":
            obj = TaskResult.objects.get(id=obj['id'])
            return TaskResultVerboseSerializer(obj, context=self.context).to_representation(obj)
        elif obj['type'] == "media":
            obj = MediaResult.objects.get(id=obj['id'])
            return MediaResultVerboseSerializer(context=self.context).to_representation(obj)
        else:
            return super(ResultsSerializer, self).to_representation(obj)


    def to_representation(self, obj):
        """
        Because Results is Polymorphic
        """
        if isinstance(obj, Result):
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
        else:
            if obj['type'] == "sensor":
                obj = SensorResult.objects.get(id=obj['id'])
                return SensorResultVerboseSerializer(obj, context=self.context).to_representation(obj)
            elif obj['type'] == "question":
                obj = QuestionResult.objects.get(id=obj['id'])
                return QuestionResultVerboseSerializer(obj, context=self.context).to_representation(obj)
            elif obj['type'] == "task":
                obj = TaskResult.objects.get(id=obj['id'])
                return TaskResultVerboseSerializer(obj, context=self.context).to_representation(obj)
            elif obj['type'] == "media":
                obj = MediaResult.objects.get(id=obj['id'])
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

    def create(self, validated_data):

        participant = validated_data.pop('participant')
        event = validated_data.pop('event')
        event_id = event['id']
        event = Event.objects.get(id=event_id)

        results_data = validated_data.pop('results')

        results = []
        for r in results_data:
            if r['type'] == "media":
                new = MediaResultVerboseSerializer()
            if r['type'] == "question":
                new = QuestionResultVerboseSerializer()
            if r['type'] == "task":
                new = TaskResultVerboseSerializer()
            if r['type'] == "sensor":
                new = SensorResultVerboseSerializer()

            results.append(new.create(r))

        result_session = ResultSession.objects.create(
            started=validated_data['started'],
            ended=validated_data['ended'],
            event=event,
            participant= Participant.objects.get(id=participant['id'])
            )

        for r in results:
            result_session.results.add(r)

        result_session.save()
        return result_session



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

    def create(self, validated_data):
        intervention = validated_data.pop('media')
        media_id = intervention["id"]

        result = MediaResult.objects.create(
            started=self.data["started"],
            ended=self.data["ended"],
            type=self.data["type"],
            media=MediaIntervention.objects.get(id=media_id),
            urlForDataFile=self.data["urlForDataFile"]
            )

        return result

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

    def create(self, validated_data):
        intervention = validated_data.pop('sensor')
        sensor_id = intervention["id"]

        result = SensorResult.objects.create(
            started=self.data["started"],
            ended=self.data["ended"],
            type=self.data["type"],
            sensor=Sensor.objects.get(id=sensor_id),
            urlForDataFile=self.data["urlForDataFile"]
            )

        return result

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

    def create(self, validated_data):
        intervention = validated_data.pop('task')
        task_id = intervention["id"]

        result = TaskResult.objects.create(
            started=self.data["started"],
            ended=self.data["ended"],
            type=self.data["type"],
            task=TaskIntervention.objects.get(id=task_id),
            urlForDataFile=self.data["urlForDataFile"]
            )

        return result

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
        question_id = intervention["id"]

        result = QuestionResult.objects.create(
            started=self.data["started"],
            ended=self.data["ended"],
            type=self.data["type"],
            question=QuestionIntervention.objects.get(id=question_id),
            answer=self.data["answer"]
            )

        return result

