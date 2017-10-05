# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from event_section.models import ActiveEvent, Event

from trigger_section.models import EventTrigger as Trigger
from intervation_section.models import *
from sensor_section.models import Sensor
from result_section.models import *


from result_section.serializers import *
from trigger_section.serializers import EventTriggerSerializer;
from sensor_section.serializers import SensorSerializer
from intervation_section.serializers import *

# PASSANDO SOMENTE O ID

class EventSerializer(serializers.ModelSerializer):

    sensors = SensorSerializer(many=True)

    class Meta:
        model = Event
        fields = ('id', 'type', 'title', 'description', 'sensors'
        )

    def to_representation(self, obj):
        """
        Because GalleryItem is Polymorphic
        """
        if obj.type == "active":
            obj = ActiveEvent.objects.get(id=obj.id)
            return ActiveEventReadSerializer(context=self.context).to_representation(obj)
        else:
            return super(EventSerializer, self).to_representation(obj)

class EventVerboseSerializer(serializers.ModelSerializer):

    results = ResultsSerializer(many=True)
    triggers = EventTriggerSerializer(many=True)
    sensors = SensorSerializer(many=True)

    interventions = InterventionSerializer(many=True)

    class Meta:
        model = Event
        fields = ('id', 'type', 'title', 'description',
        'triggers', 'sensors', 'interventions', 'results'
        )

    def to_representation(self, obj):
        """
        Because GalleryItem is Polymorphic
        """
        if obj.type == "active":
            obj = ActiveEvent.objects.get(id=obj.id)
            return ActiveEventVerboseSerializer(context=self.context).to_representation(obj)
        else:
            return super(EventSerializer, self).to_representation(obj)




class ActiveEventSerializer(serializers.ModelSerializer):
    # just id without, dict with
    # participant = ParticipantSerializer(read_only=True)
    # media = MediaInterventionSerializer()

    class Meta:
        model = ActiveEvent
        fields = ('id', 'type', 'title' , 'description',
           'results',
           'triggers', 'sensors', 'interventions' )

class ActiveEventVerboseSerializer(serializers.ModelSerializer):
    # just id without, dict with
    results = ResultsSerializer(many=True)

    triggers = EventTriggerSerializer(many=True)
    sensors = SensorSerializer(many=True)

    interventions = InterventionSerializer(many=True)

    class Meta:
        model = ActiveEvent
        fields = ('id', 'type', 'title' , 'description',
           'results',
           'triggers', 'sensors',
           'interventions')

    def create(self, validated_data):
        activeevent = self.saving_data(validated_data)

        return activeevent

    def saving_data(self, validated_data):
        interventions_data = validated_data.pop('interventions')
        triggers_data = validated_data.pop('triggers')
        sensors_data = validated_data.pop('sensors')
        results_data = validated_data.pop('results')

        triggers = []
        for t in triggers_data:
            triggers.append(Trigger.objects.create(**t))

        sensors = []
        for s in sensors_data:
            sensors.append(Sensor.objects.create(**s))

        interventions = []
        for i in interventions_data:
            medias_data = i.pop('medias')
            # print medias_data
            arr = []
            for media_data in medias_data:
                n = MediaPresentation.objects.create(**media_data)
                arr.append(n.id)
            if i['type'] == "empty":
                interventions.append(EmptyIntervention.objects.create(**i))
            if i['type'] == "media":
                interventions.append(MediaIntervention.objects.create(**i))
            if i['type'] == "task":
                interventions.append(TaskIntervention.objects.create(**i))
            if i['type'] == "question":
                interventions.append(QuestionIntervention.objects.create(**i))

            interventions[-1].medias = arr
            interventions[-1].save()

        activeevent = ActiveEvent.objects.create(
            **validated_data
            )

        for i in interventions:
            activeevent.interventions.add(i)

        for s in sensors:
            activeevent.sensors.add(s)

        for t in triggers:
            activeevent.triggers.add(t)

        activeevent.save()

        return activeevent