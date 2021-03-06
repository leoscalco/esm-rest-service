# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from program_section.serializers import *


class ProgramList(APIView):
    """
    List all program, or create a new program
    """

    def get(self, request, format=None):
        program = Program.objects.all()
        if (request.GET.get('verbose') == 'true'):
            serializer = ProgramVerboseSerializer(program, many=True)
        else:
            serializer = ProgramSerializer(program, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):

        if (request.GET.get('verbose') == 'true'):
            serializer = ProgramVerboseSerializer(data=request.data)
        else:
            serializer = ProgramSerializer(data=request.data)

        # serializer = ProgramWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProgramDetail(APIView):
    """
    Retrieve, update or delete a program instance.
    """

    def get_object(self, pk):
        try:
            return Program.objects.get(pk=pk)
        except Program.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        program = self.get_object(pk)
        if (request.GET.get('verbose') == 'true'):
            serializer = ProgramVerboseSerializer(program)
        else:
            serializer = ProgramSerializer(program)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        program = self.get_object(pk)

        if (request.GET.get('verbose') == 'true'):
            serializer = ProgramVerboseSerializer(program, data=request.data)
        else:
            serializer = ProgramSerializer(program, data=request.data)

        # serializer = ProgramSerializer(program, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        program = self.get_object(pk)
        Program.delete(program)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProgramsByEmail(APIView):

    def get(self, request, format=None):
        observer = Observer.objects.get(email=request.GET.get('email'))
        try:
            queryset = Program.objects.filter(observers__id=observer.id)
            if not len(queryset):
                return Response({"error": "Observer without programs."}, status=status.HTTP_404_NOT_FOUND)
            else:
                serializer = ProgramVerboseSerializer(queryset, many=True)
                return Response(serializer.data)
        except Program.DoesNotExist:
            return Response({"error": "E-mail not found."}, status=status.HTTP_404_NOT_FOUND)


class ProgramsByParticipantEmail(APIView):

    def get(self, request, format=None):
        participant = Participant.objects.get(email=request.GET.get('email'))
        try:
            queryset = Program.objects.filter(participants__id=participant.id)
            if not len(queryset):
                return Response({"error": "Participant without programs."}, status=status.HTTP_404_NOT_FOUND)
            else:
                serializer = ProgramVerboseSerializer(queryset, many=True)
                return Response(serializer.data)
        except Program.DoesNotExist:
            return Response({"error": "E-mail not found."}, status=status.HTTP_404_NOT_FOUND)
