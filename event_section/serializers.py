# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from event_section.models import ActiveEvent, Event

from trigger_section.models import EventTrigger as Trigger
from intervation_section.models import *
from sensor_section.models import Sensor
# from result_section.models import *


from result_section.serializers import *
from trigger_section.serializers import EventTriggerSerializer;
from sensor_section.serializers import SensorSerializer
from intervation_section.serializers import *

# PASSANDO SOMENTE O ID

class EventSerializer(serializers.ModelSerializer):

    sensors = SensorSerializer(many=True)

    class Meta:
        model = Event
        fields = ('id', 'type', 'title', 'group' 'description', 'sensors'
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

class EventVerboseSerializer(serializers.ModelSerializer):

    # results = ResultsSerializer(many=True)
    triggers = EventTriggerSerializer(many=True)
    sensors = SensorSerializer(many=True)

    interventions = InterventionSerializer(many=True)

    class Meta:
        model = Event
        fields = ('id', 'type', 'title', 'description',
        'triggers', 'sensors', 'interventions'
        )

    def to_internal_value(self, obj):
        """
        Because GalleryItem is Polymorphic
        """
        print "Aaaaa"
        if obj['type'] == "active":
            obj = ActiveEvent.objects.get(id=obj['id'])
            return ActiveEventVerboseSerializer(context=self.context).to_representation(obj)
        else:
            return super(EventSerializer, self).to_representation(obj)


    def to_representation(self, obj):
        """
        Because GalleryItem is Polymorphic
        """
        if isinstance(obj, Event):
            if obj.type == "active":
                obj = ActiveEvent.objects.get(id=obj.id)
                return ActiveEventVerboseSerializer(context=self.context).to_representation(obj)
            else:
                return super(EventSerializer, self).to_representation(obj)
        else:
            if obj['type'] == "active":
                obj = ActiveEvent.objects.get(id=obj['id'])
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
           'triggers', 'sensors', 'interventions' )

class ActiveEventVerboseSerializer(serializers.ModelSerializer):
    # just id without, dict with
    # results = ResultsSerializer(many=True)
    # id = serializers.IntegerField(required=False)
    triggers = EventTriggerSerializer(many=True)
    sensors = SensorSerializer(many=True)

    interventions = InterventionSerializer(many=True)

    class Meta:
        model = ActiveEvent
        fields = ('id', 'type', 'title' , 'description',
           'triggers', 'sensors',
           'interventions')

    extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }

    def create(self, validated_data):
        activeevent = self.saving_data(validated_data)
        return activeevent

    def update(self, instance, validated_data):

        instance.type = validated_data.get('type', instance.type)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        interventions_data = validated_data.pop('interventions')
        triggers_data = validated_data.pop('triggers')
        sensors_data = validated_data.pop('sensors')

        for trigger in triggers_data:
            t = Trigger.objects.create(
                **trigger
            )
            instance.triggers.add(t)

        for sensor in sensors_data:
            s = Sensor.objects.create(
                **sensor
            )
            instance.sensors.add(s)

        for intervention in interventions_data:
            medias_data = intervention.pop('medias')
            arr = []
            for media_data in medias_data:
                n = MediaPresentation.objects.create(**media_data)
                arr.append(n.id)
            if intervention['type'] == "empty":
                i = EmptyIntervention.objects.create(**intervention)
            if intervention['type'] == "media":
                i =MediaIntervention.objects.create(**iintervention)
            if intervention['type'] == "task":
                i = TaskIntervention.objects.create(**intervention)
            if intervention['type'] == "question":
                i = QuestionIntervention.objects.create(**intervention)

            i.medias = arr
            instance.interventions.add(i)

        instance.save()
        return instance

    def saving_data(self, validated_data):
        if (len(Event.objects.all()) == 0):
            validated_data['id'] = 1
        else:
            validated_data['id'] = Event.objects.all().latest('id').id

        interventions_data = validated_data.pop('interventions')
        triggers_data = validated_data.pop('triggers')
        sensors_data = validated_data.pop('sensors')
        # results_data = validated_data.pop('results')

        triggers = []
        for t in triggers_data:
            ts = EventTriggerSerializer()
            ts.create(t)
            triggers.append(EventTrigger.objects.all().latest('id'))

            # triggers.append(Trigger.objects.create(**t))

        sensors = []
        for s in sensors_data:
            ss = SensorSerializer()
            ss.create(s)
            sensors.append(Sensor.objects.all().latest('id'))
            # sensors.append(Sensor.objects.create(**s))

        interventions = []
        for i in interventions_data:
            # medias_data = i.pop('medias')
            # # print medias_data
            # arr = []
            # for media_data in medias_data:
                # media_data['id'] = MediaPresentation.objects.all().latest('id').id + 1
                # n = MediaPresentation.objects.create(**media_data)
            #     arr.append(n.id)

            if i['type'] == "empty":
                emps = EmptyInterventionSerializer()
                emps.create(i)
                # triggers.append(EventTrigger.objects.all().latest('id'))

                interventions.append(
                    Intervention.objects.all().latest('id')
                )
            if i['type'] == "task":
                tasks = TaskInterventionSerializer()
                tasks.create(i)
                interventions.append(Intervention.objects.all().latest('id'))

            if i['type'] == "media":
                mediaser = MediaInterventionSerializer()
                mediaser.create(i)
                interventions.append(Intervention.objects.all().latest('id'))

            if i['type'] == "question":
                ques = QuestionInterventionSerializer()
                ques.create(i)
                interventions.append(Intervention.objects.all().latest('id'))

            # for a in arr:
            #     interventions[-1].medias.add(a)
            # interventions[-1].medias = arr
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