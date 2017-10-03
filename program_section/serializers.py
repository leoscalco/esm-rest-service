# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from program_section.models import *
from user_section.serializers import *
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
    observers = ObserverReadSerializer(many=True)
    events = EventSerializer(many=True)

    class Meta:
        model = Program
        fields = (
            'id', 'title', 'description', 'starts', 'ends', 'updateDate',
            'participants', 'observers', 'events'
        )