# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
from intervation_section.serializers import EmptyInterventionSerializer, TaskInterventionSerializer, MediaInterventionSerializer, QuestionInterventionSerializer
from intervation_section.models import EmptyIntervention, TaskIntervention, MediaIntervention, QuestionIntervention

class EmptyInterventionList(APIView):
    """
    List all emptyInterventions, or create a new eventTrigger
    """
    def get(self, request, format=None):
        interventions = EmptyIntervention.objects.all()
        serializer = EmptyInterventionSerializer(interventions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmptyInterventionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmptyInterventionDetail(APIView):
    """
    Retrieve, update or delete a emptyIntervention instance.
    """
    def get_object(self, pk):
        try:
            return EmptyIntervention.objects.get(pk=pk)
        except EmptyIntervention.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        intervention = self.get_object(pk)
        serializer = EmptyInterventionSerializer(intervention)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        intervention = self.get_object(pk)
        serializer = EmptyInterventionSerializer(intervention, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        intervention = self.get_object(pk)
        EmptyIntervention.delete(intervention)
        return Response(status=status.HTTP_204_NO_CONTENT)

class TaskInterventionList(APIView):
    """
    List all taskInterventions, or create a new taskIntervention
    """
    def get(self, request, format=None):
        interventions = TaskIntervention.objects.all()
        serializer = TaskInterventionSerializer(interventions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskInterventionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskInterventionDetail(APIView):
    """
    Retrieve, update or delete a emptyIntervention instance.
    """
    def get_object(self, pk):
        try:
            return TaskIntervention.objects.get(pk=pk)
        except TaskIntervention.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        intervention = self.get_object(pk)
        serializer = TaskInterventionSerializer(intervention)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        intervention = self.get_object(pk)
        serializer = TaskInterventionSerializer(intervention, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        intervention = self.get_object(pk)
        TaskIntervention.delete(intervention)
        return Response(status=status.HTTP_204_NO_CONTENT)

class MediaInterventionList(APIView):
    """
    List all mediaInterventions, or create a new mediaIntervention
    """
    def get(self, request, format=None):
        interventions = MediaIntervention.objects.all()
        serializer = MediaInterventionSerializer(interventions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MediaInterventionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MediaInterventionDetail(APIView):
    """
    Retrieve, update or delete a mediaIntervention instance.
    """
    def get_object(self, pk):
        try:
            return MediaIntervention.objects.get(pk=pk)
        except MediaIntervention.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        intervention = self.get_object(pk)
        serializer = MediaInterventionSerializer(intervention)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        intervention = self.get_object(pk)
        serializer = MediaInterventionSerializer(intervention, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        intervention = self.get_object(pk)
        MediaIntervention.delete(intervention)
        return Response(status=status.HTTP_204_NO_CONTENT)

class QuestionInterventionList(APIView):
    """
    List all questionInterventions, or create a new mediaIntervention
    """
    def get(self, request, format=None):
        interventions = QuestionIntervention.objects.all()
        serializer = QuestionInterventionSerializer(interventions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionInterventionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionInterventionDetail(APIView):
    """
    Retrieve, update or delete a mediaIntervention instance.
    """
    def get_object(self, pk):
        try:
            return QuestionIntervention.objects.get(pk=pk)
        except QuestionIntervention.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        intervention = self.get_object(pk)
        serializer = QuestionInterventionSerializer(intervention)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        intervention = self.get_object(pk)
        serializer = QuestionInterventionSerializer(intervention, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        intervention = self.get_object(pk)
        QuestionIntervention.delete(intervention)
        return Response(status=status.HTTP_204_NO_CONTENT)
