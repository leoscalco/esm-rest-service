# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from intervation_section.models import *

class MediaPresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaPresentation
        fields = ('id', 'type', 'mediaUrl')

class ComplexConditionSerializer(serializers.ModelSerializer):
    # contacts = ObserverContactsSerializer(many=True)

    class Meta:
        model = ComplexCondition
        fields = ('id', 'value', 'type', 'condition', 'next')

class JSONSerializerField(serializers.Field):
    """ Serializer for JSONField -- required to make field writable"""
    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return value

# class MAPConditionsSerializer(serializers.ModelSerializer):
#      class Meta:
#         model = MAP_conditions
#         fields = ('id', 'answer', 'value')

# class ARRAY_OptionSerialzer(serializers.ModelSerializer):
#     class Meta:
#         model = ARRAY_option
#         fields = ('id', 'option')

class InterventionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Intervention
        fields = ('id', 'type', 'statement','medias',
            'orderPosition', 'first', 'next', 'obligatory'
        )

    def to_representation(self, obj):
        """
        Because GalleryItem is Polymorphic
        """
        if obj.type == "empty":
            return EmptyInterventionSerializer(obj, context=self.context).to_representation(obj)
        elif obj.type == "question":
           return QuestionInterventionSerializer(obj, context=self.context).to_representation(obj)
        elif obj.type == "task":
           return TaskInterventionSerializer(obj, context=self.context).to_representation(obj)
        elif obj.type == "media":
           return MediaInterventionSerializer(obj, context=self.context).to_representation(obj)

        return super(InterventionSerializer, self).to_representation(obj)

class EmptyInterventionSerializer(serializers.ModelSerializer):
    medias = MediaPresentationSerializer(many=True)

    class Meta:
        model = EmptyIntervention
        fields = ('id', 'type', 'statement','medias',
            'orderPosition', 'first', 'next', 'obligatory'
        )

    def create(self, validated_data):
        medias_data = validated_data.pop('medias')
        arr = []
        for media_data in medias_data:
            n = MediaPresentation.objects.create(**media_data)
            arr.append(n.id)
        # validated_data['medias'] = arr

        empty_intervention = EmptyIntervention.objects.create(**validated_data)
        empty_intervention.medias = arr
        empty_intervention.save()
        return empty_intervention

class TaskInterventionSerializer(serializers.ModelSerializer):
    medias = MediaPresentationSerializer(many=True)

    class Meta:
        model = TaskIntervention
        fields = ('id', 'type', 'statement','medias',
            'orderPosition', 'first', 'next', 'obligatory',
            'appPackage'
        )

    def create(self, validated_data):
        medias_data = validated_data.pop('medias')
        arr = []
        for media_data in medias_data:
            n = MediaPresentation.objects.create(**media_data)
            arr.append(n.id)
        # validated_data['medias'] = arr
        print validated_data
        intervention = TaskIntervention.objects.create(**validated_data)
        intervention.medias = arr
        intervention.save()
        return intervention

class MediaInterventionSerializer(serializers.ModelSerializer):
    medias = MediaPresentationSerializer(many=True)

    class Meta:
        model = MediaIntervention
        fields = ('id', 'type', 'statement', 'medias',
            'orderPosition', 'first', 'next', 'obligatory',
            'mediaType'
        )

    def create(self, validated_data):
        medias_data = validated_data.pop('medias')
        arr = []
        for media_data in medias_data:
            n = MediaPresentation.objects.create(**media_data)
            arr.append(n.id)
        # validated_data['medias'] = arr

        intervention = MediaIntervention.objects.create(**validated_data)
        intervention.medias = arr
        intervention.save()
        return intervention

class QuestionInterventionSerializer(serializers.ModelSerializer):
    medias = MediaPresentationSerializer(many=True)
    complexConditions = ComplexConditionSerializer(many=True)
    options = JSONSerializerField()
    conditions = JSONSerializerField()

    class Meta:
        model = QuestionIntervention
        fields = ('id', 'type', 'statement', 'medias',
            'orderPosition', 'first', 'next', 'obligatory',
            'questionType', 'options', 'conditions', 'complexConditions'
        )

    def create(self, validated_data):
        medias_data = validated_data.pop('medias')
        complex_cond_data = validated_data.pop('complexConditions')
        # cond_data = validated_data.pop('conditions')
        # options_data = validated_data.pop('options')

        arr_medias = []
        arr_compl = []
        arr_cond = []
        arr_opt = []

        intervention = QuestionIntervention.objects.create(**validated_data)

        for media_data in medias_data:
            n = MediaPresentation.objects.create(**media_data)
            arr_medias.append(n.id)

        # for c in cond_data:
        #     n = MAP_conditions.objects.create(questionIntervention=intervention, **c)
        #     arr_cond.append(n.id)

        # for o in options_data:
        #     n = ARRAY_option.objects.create(questionIntervention=intervention, **o)
        #     arr_opt.append(n.id)

        for cc in complex_cond_data:
            n = ComplexCondition.objects.create(**cc)
            arr_compl.append(n.id)

        intervention.medias = arr_medias
        intervention.complexConditions = arr_compl
        # intervention.options = arr_opt
        # intervention.conditions = arr_cond

        intervention.save()
        return intervention