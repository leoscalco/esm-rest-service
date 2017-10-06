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



        # return super(InterventionSerializer, self).to_representation(obj)

class InterventionSerializer(serializers.ModelSerializer):

    medias = MediaPresentationSerializer(many=True)
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
            obj = EmptyIntervention.objects.get(id=obj.id)
            return EmptyInterventionSerializer(obj, context=self.context).to_representation(obj)
        elif obj.type == "question":
            obj = QuestionIntervention.objects.get(id=obj.id)
            return QuestionInterventionSerializer(obj, context=self.context).to_representation(obj)
        elif obj.type == "task":
            obj = TaskIntervention.objects.get(id=obj.id)
            return TaskInterventionSerializer(obj, context=self.context).to_representation(obj)
        elif obj.type == "media":
            obj = MediaIntervention.objects.get(id=obj.id)
            return MediaInterventionSerializer(context=self.context).to_representation(obj)
        else:
            return super(InterventionSerializer, self).to_representation(obj)

class EmptyInterventionSerializer(serializers.ModelSerializer):
    medias = MediaPresentationSerializer(many=True)

    class Meta:
        model = EmptyIntervention
        fields = ('id', 'type', 'statement','medias',
            'orderPosition', 'first', 'next', 'obligatory'
        )

    def create(self, validated_data):
        if (len(Intervention.objects.all()) == 0):
            validated_data['id'] = 1
        else:
            validated_data['id'] = Intervention.objects.all().latest('id').id

        medias_data = validated_data.pop('medias')
        validated_data['id'] += 1
        arr = []
        for media_data in medias_data:
            if (len(MediaPresentation.objects.all()) == 0):
                media_data['id'] = 1
            else:
                media_data['id'] = MediaPresentation.objects.all().latest('id').id
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
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }

    def create(self, validated_data):
        if (len(Intervention.objects.all()) == 0):
            validated_data['id'] = 1
        else:
            validated_data['id'] = Intervention.objects.all().latest('id').id

        medias_data = validated_data.pop('medias')
        arr = []
        for media_data in medias_data:
            if (len(MediaPresentation.objects.all()) == 0):
                media_data['id'] = 1
            else:
                media_data['id'] = MediaPresentation.objects.all().latest('id').id
            n = MediaPresentation.objects.create(**media_data)
            arr.append(n.id)
        # validated_data['medias'] = arr

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
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }

    def create(self, validated_data):
        if (len(Intervention.objects.all()) == 0):
            validated_data['id'] = 1
        else:
            validated_data['id'] = Intervention.objects.all().latest('id').id

        medias_data = validated_data.pop('medias')
        arr = []
        for media_data in medias_data:
            if (len(MediaPresentation.objects.all()) == 0):
                media_data['id'] = 1
            else:
                media_data['id'] = MediaPresentation.objects.all().latest('id').id
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
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }

    def create(self, validated_data):
        if (len(Intervention.objects.all()) == 0):
            validated_data['id'] = 1
        else:
            validated_data['id'] = Intervention.objects.all().latest('id').id

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
            if (len(MediaPresentation.objects.all()) == 0):
                media_data['id'] = 1
            else:
                media_data['id'] = MediaPresentation.objects.all().latest('id').id
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