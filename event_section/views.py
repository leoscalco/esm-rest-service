# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
from event_section.serializers import *
from event_section.models import ActiveEvent


class ActiveEventList(APIView):
    """
    List all activeEvent, or create a new activeEvent
    """
    def get(self, request, format=None):
        event = ActiveEvent.objects.all()
        serializer = ActiveEventReadSerializer(event, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ActiveEventWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActiveEventDetail(APIView):
    """
    Retrieve, update or delete a ActiveEvent instance.
    """
    def get_object(self, pk):
        try:
            return ActiveEvent.objects.get(pk=pk)
        except ActiveEvent.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = ActiveEventReadSerializer(event)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = ActiveEventWriteSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        ActiveEvent.delete(event)
        return Response(status=status.HTTP_204_NO_CONTENT)