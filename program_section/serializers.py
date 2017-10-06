# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from program_section.models import *
from user_section.models import *
from event_section.models import *
from user_section.serializers import *
from event_section.serializers import *

class ProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Program
        fields = (
            'id', 'title', 'description', 'starts', 'ends', 'updateDate',
            'participants', 'observers', 'events'
        )

class ProgramVerboseSerializer(serializers.ModelSerializer):

    participants = ParticipantSerializer(many=True)
    observers = ObserverVerboseSerializer(many=True)
    events = EventVerboseSerializer(many=True)

    class Meta:
        model = Program
        fields = (
            'id', 'title', 'description', 'starts', 'ends', 'updateDate',
            'participants', 'observers', 'events'
        )

    def create(self, validated_data):
        print validated_data

        participants_data = validated_data.pop('participants')
        observers_data = validated_data.pop('observers')
        events_data = validated_data.pop('events')

        participants = []
        for p in participants_data:
            participants.append(Participant.objects.get(id=p['id']))

        observers = []
        for o in observers_data:
            cs = o.pop('contacts')
            print o
            observers.append(Observer.objects.get(id=o['id']))
            for c in cs:
                print c
                p = Participant.objects.get(id=c['id'])
                observers[-1].contacts.add(p)
            observers[-1].save()

        events = []
        for e in events_data:
            if e['type'] == "active":
                aes = ActiveEventVerboseSerializer()
                # if serializer.is_valid():
                #     serializer.save()
                aes.saving_data(e)
                events.append(Event.objects.all().latest('id'))

        program = Program.objects.create(
            **validated_data
            )

        for p in participants:
            program.participants.add(p)

        for o in observers:
            program.observers.add(o)

        for e in events:
            program.events.add(e)

        program.save()

        return program

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.starts = validated_data.get('starts', instance.starts)
        instance.ends = validated_data.get('ends', instance.ends)
        instance.updateDate = validated_data.get('updateDate', instance.updateDate)
        instance.save()

        participants_data = validated_data.pop('participants')
        observers_data = validated_data.pop('observers')
        events_data = validated_data.pop('events')

        # for participant in participants_data:
        #     p = Participant.objects.create(
        #         **participant
        #     )
        #     instance.triggers.add(t)

        for event in events_data:
            if event['type'] == "active":
                aes = ActiveEventVerboseSerializer()
                aes.saving_data(event)
                instance.events.add(Event.objects.all().latest('id'))

        instance.save()

        return instance
