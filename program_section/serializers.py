# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from program_section.models import *
from user_section.serializers import ParticipantSerializer, ObserverSerializer
from event_section.serializers import ActiveEventReadSerializer, EventSerializer

class ProgramWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Program
        fields = (
            'id', 'title', 'description', 'starts', 'ends', 'updateDate',
            'participants', 'observers', 'events'
        )

class ProgramReadSerializer(serializers.ModelSerializer):

    participants = ParticipantSerializer(many=True)
    observers = ObserverSerializer(many=True)
    events = EventReadSerializer(many=True)

    class Meta:
        model = Program
        fields = (
            'id', 'title', 'description', 'starts', 'ends', 'updateDate',
            'participants', 'observers', 'events'
        )