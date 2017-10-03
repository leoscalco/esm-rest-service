# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
from result_section.serializers import *
from result_section.models import MediaResult, TaskResult, SensorResult, QuestionResult

class ResultsList(APIView):

    def get(self, request, format=None):
        results = Result.objects.all()
        serializer = ResultsSerializer(results, many=True)
        return Response(serializer.data)

class MediaResultList(APIView):
    """
    List all taskresults, or create a new taskresult
    """
    def get(self, request, format=None):
        result = MediaResult.objects.all()
        serializer = MediaResultReadSerializer(result, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MediaResultWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MediaResultDetail(APIView):
    """
    Retrieve, update or delete a mediaResult instance.
    """
    def get_object(self, pk):
        try:
            return MediaResult.objects.get(pk=pk)
        except MediaResult.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        result = self.get_object(pk)
        serializer = MediaResultReadSerializer(result)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        result = self.get_object(pk)
        serializer = MediaResultWriteSerializer(result, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        result = self.get_object(pk)
        MediaResult.delete(result)
        return Response(status=status.HTTP_204_NO_CONTENT)

class TaskResultList(APIView):
    """
    List all taskresult, or create a new taskresult
    """
    def get(self, request, format=None):
        result = TaskResult.objects.all()
        serializer = TaskResultReadSerializer(result, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskResultWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskResultDetail(APIView):
    """
    Retrieve, update or delete a taskresult instance.
    """
    def get_object(self, pk):
        try:
            return TaskResult.objects.get(pk=pk)
        except TaskResult.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        result = self.get_object(pk)
        serializer = TaskResultReadSerializer(result)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        result = self.get_object(pk)
        serializer = TaskResultWriteSerializer(result, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        result = self.get_object(pk)
        TaskResult.delete(result)
        return Response(status=status.HTTP_204_NO_CONTENT)


class SensorResultList(APIView):
    """
    List all sensorresults, or create a new sensorresult
    """
    def get(self, request, format=None):
        result = SensorResult.objects.all()
        serializer = SensorResultReadSerializer(result, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SensorResultWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SensorResultDetail(APIView):
    """
    Retrieve, update or delete a sensorresult instance.
    """
    def get_object(self, pk):
        try:
            return SensorResult.objects.get(pk=pk)
        except SensorResult.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        result = self.get_object(pk)
        serializer = SensorResultReadSerializer(result)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        result = self.get_object(pk)
        serializer = SensorResultWriteSerializer(result, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        result = self.get_object(pk)
        SensorResult.delete(result)
        return Response(status=status.HTTP_204_NO_CONTENT)

class QuestionResultList(APIView):
    """
    List all sensorresults, or create a new sensorresult
    """
    def get(self, request, format=None):
        result = QuestionResult.objects.all()
        serializer = QuestionResultReadSerializer(result, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionResultWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionResultDetail(APIView):
    """
    Retrieve, update or delete a sensorresult instance.
    """
    def get_object(self, pk):
        try:
            return QuestionResult.objects.get(pk=pk)
        except QuestionResult.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        result = self.get_object(pk)
        serializer = QuestionResultReadSerializer(result)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        result = self.get_object(pk)
        serializer = QuestionResultWriteSerializer(result, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        result = self.get_object(pk)
        QuestionResult.delete(result)
        return Response(status=status.HTTP_204_NO_CONTENT)