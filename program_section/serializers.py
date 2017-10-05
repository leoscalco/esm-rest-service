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
        print "   - - - - - "
        print events_data

        participants = []
        for p in participants_data:
            participants.append(Participant.objects.get(id=p['id']))

        observers = []
        for o in observers_data:
            cs = o.pop('contacts')
            observers.append(Observer.objects.get(id=p['id']))
            for i in range(len(cs)):
                print i
                p = Participant.objects.get(email=cs[i]['email'])
                print p
                observers[-1].contacts.add(p)
            observers[-1].save()

        events = []
        for e in events_data:
            if e['type'] == "active":
                aes = ActiveEventReadSerializer()
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