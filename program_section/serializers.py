# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from program_section.models import *
from user_section.serializers import ParticipantSerializer, ObserverSerializer
from event_section.serializers import ActiveEventReadSerializer

class ProgramWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Program
        fields = (
            'id', 'title', 'description', 'starts', 'ends', 'update_date',
            'participants', 'observers', 'active_events'
        )

class ProgramReadSerializer(serializers.ModelSerializer):

    participants = ParticipantSerializer(many=True)
    observers = ObserverSerializer(many=True)
    active_events = ActiveEventReadSerializer(many=True)

    class Meta:
        model = Program
        fields = (
            'id', 'title', 'description', 'starts', 'ends', 'update_date',
            'participants', 'observers', 'active_events'
        )