# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, mixins

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from user_section.serializers import *
from user_section.models import Observer, Participant

class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows user to be viewed or edited."""

    queryset = User.objects.all().order_by('-date_joined')
    serializers_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """API endpoint that allows groups to be viewed or edited."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ObserverList(APIView):
    """
    List all persons, or create a new person
    """
    def get(self, request, format=None):
        persons = Observer.objects.all()
        if (request.GET.get('verbose') == 'true'):
            serializer = ObserverVerboseSerializer(persons, many=True)
        else:
            serializer = ObserverSerializer(persons, many=True)
        # serializer = ObserverVerboseSerializer(persons, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        if (request.GET.get('verbose') == 'true'):
            serializer = ObserverVerboseSerializer(data=request.data)
        else:
            serializer = ObserverSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ObserverDetail(APIView):
    """
    Retrieve, update or delete a observer instance.
    """
    def get_object(self, pk):
        try:
            return Observer.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        person = self.get_object(pk)
        if (request.GET.get('verbose') == 'true'):
            serializer = ObserverVerboseSerializer(person)
        else:
            serializer = ObserverSerializer(person)
        # serializer = ObserverReadSerializer(person)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        person = self.get_object(pk)

        if (request.GET.get('verbose') == 'true'):
            serializer = ObserverVerboseSerializer(person, data=request.data)
        else:
            serializer = ObserverSerializer(person, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        person = self.get_object(pk)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ObserverByEmail(APIView):

    def get(self, request, format=None):
        try:
            queryset = Observer.objects.get(email=request.GET.get('email'))
            serializer = ObserverReadSerializer(queryset)
            return Response(serializer.data)
        except Observer.DoesNotExist:
            return Response({"error":"E-mail not found."}, status=status.HTTP_404_NOT_FOUND)


class ParticipantByEmail(APIView):

   def get(self, request, format=None):
        try:
            queryset = Participant.objects.get(email=request.GET.get('email'))
            serializer = ParticipantSerializer(queryset)
            return Response(serializer.data)
        except Participant.DoesNotExist:
            return Response({"error":"E-mail not found."}, status=status.HTTP_404_NOT_FOUND)


class ParticipantList(APIView):
    """
    List all persons, or create a new person
    """
    def get(self, request, format=None):
        persons = Participant.objects.all()
        serializer = ParticipantSerializer(persons, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ParticipantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ParticipantDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Participant.objects.get(pk=pk)
        except Participant.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        person = self.get_object(pk)
        serializer = ParticipantSerializer(person)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        person = self.get_object(pk)
        serializer = ParticipantSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        person = self.get_object(pk)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

