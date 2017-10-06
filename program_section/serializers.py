# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from program_section.models import *
from user_section.models import *
from event_section.models import *
from user_section.serializers import *
from event_section.serializers import *
from django.db import IntegrityError, transaction

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
        try:
            with transaction.atomic():

                participants_data = validated_data.pop('participants')
                observers_data = validated_data.pop('observers')
                events_data = validated_data.pop('events')

                participants = []
                for p in participants_data:
                    participants.append(
                        Participant.objects.create(
                            name=p['name'], email=p['email'])
                        )

                observers = []
                for o in observers_data:
                    cs = o.pop('contacts')

                    observers.append(Observer.objects.create(
                        role=o['role'], name=o['name'], email=o['email']
                        ))
                    for c in cs:
                        if Participant.objects.filter(email=c['email']).exists():
                            p = Participant.objects.get(email=c['email'])
                        else:
                            p = Participant.objects.create(
                                name=c['name'], email=c['email']
                                )
                        observers[-1].contacts.add(p)
                    observers[-1].save()

                events = []
                for e in events_data:
                    if e['type'] == "active":
                        aes = ActiveEventVerboseSerializer()
                        # if serializer.is_valid():
                        #     serializer.save()
                        # aes.saving_data(e)
                        z = aes.saving_data(e)
                        events.append(z)

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
        except IntegrityError:
            return "Error"

    def update(self, instance, validated_data):
        try:
            with transaction.atomic():
                instance.title = validated_data.get('title', instance.title)
                instance.description = validated_data.get('description', instance.description)
                instance.starts = validated_data.get('starts', instance.starts)
                instance.ends = validated_data.get('ends', instance.ends)
                instance.updateDate = validated_data.get('updateDate', instance.updateDate)
                instance.save()

                participants_data = validated_data.pop('participants')
                observers_data = validated_data.pop('observers')
                events_data = validated_data.pop('events')

                participants = []
                for p in participants_data:
                    participants.append(
                        Participant.objects.create(
                            name=p['name'], email=p['email'])
                        )

                observers = []
                for o in observers_data:
                    cs = o.pop('contacts')

                    observers.append(Observer.objects.create(
                        role=o['role'], name=o['name'], email=o['email']
                        ))
                    for c in cs:
                        if Participant.objects.filter(email=c['email']).exists():
                            p = Participant.objects.get(email=c['email'])
                        else:
                            p = Participant.objects.create(
                                name=c['name'], email=c['email']
                                )
                        observers[-1].contacts.add(p)
                    observers[-1].save()

                for p in participants:
                    instance.participants.add(p)

                for o in observers:
                    instance.observers.add(o)

                # for participant in participants_data:
                #     ps = ParticipantSerializer()
                #     # ps = ParticipantSerializer.create(
                #     #     participant
                #     # )
                #     instance.participants.add(ps.create(participant))

                # for observer in observers_data:
                #     os = ObserverVerboseSerializer()
                #     instance.observers.add(os.create(observer))

                for event in events_data:
                    if event['type'] == "active":
                        aes = ActiveEventVerboseSerializer()
                        # aes.saving_data(event)
                        instance.events.add(aes.saving_data(event))

                instance.save()

                return instance
        except IntegrityError:
            return "Error"
