# from django.contrib.auth.models import User, Group
from rest_framework import serializers

from intervention_section.models import *
from result_section.serializers import ResultsSerializer


class MediaPresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaPresentation
        fields = ('id', 'type', 'mediaUrl')
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }


class ComplexConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplexCondition
        fields = ('id', 'value', 'type', 'condition', 'next')


class JSONSerializerField(serializers.Field):
    """ Serializer for JSONField -- required to make field writable"""

    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return value


class InterventionSerializer(serializers.ModelSerializer):
    medias = MediaPresentationSerializer(many=True)

    class Meta:
        model = Intervention
        fields = ('id', 'type', 'statement', 'medias',
                  'orderPosition', 'first', 'next', 'obligatory'
                  )

    def to_internal_value(self, obj):
        """
        Because Results is Polymorphic
        """
        if obj['type'] == 'empty':
            # if obj['type'] == 'sensor'
            # self.fields += ()
            # obj = SensorResult.objects.get(id=obj['sensor'])
            return EmptyInterventionSerializer(context=self.context).to_internal_value(obj)
        elif obj['type'] == 'question':
            # obj = QuestionResult.objects.get(id=obj['question'])
            return QuestionInterventionSerializer(context=self.context).to_internal_value(obj)
        elif obj['type'] == 'task':
            # obj = TaskResult.objects.get(id=obj['id'])
            return TaskInterventionSerializer(context=self.context).to_internal_value(obj)
        elif obj['type'] == 'media':
            # obj = MediaResult.objects.get(id=obj['media'])
            return MediaInterventionSerializer(context=self.context).to_internal_value(obj)
        else:
            return super(ResultsSerializer, self).to_internal_value(obj)

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
        fields = ('id', 'type', 'statement', 'medias',
                  'orderPosition', 'first', 'next', 'obligatory'
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
            validated_data['id'] = Intervention.objects.all().latest('id').id + 1

        medias_data = validated_data.pop('medias')
        arr = []
        for media_data in medias_data:
            if (len(MediaPresentation.objects.all()) == 0):
                media_data['id'] = 1
            else:
                media_data['id'] = MediaPresentation.objects.all().latest('id').id + 1
            n = MediaPresentation.objects.create(**media_data)
            arr.append(n.id)
        # validated_data['medias'] = arr

        empty_intervention = EmptyIntervention.objects.create(**validated_data)
        empty_intervention.medias = arr
        empty_intervention.save()
        return empty_intervention

    def update(self, instance, validated_data):

        instance.statement = validated_data.get('statement')
        instance.orderPosition = validated_data.get('orderPosition')
        instance.first = validated_data.get('first')
        instance.next = validated_data.get('next')
        instance.obligatory = validated_data.get('obligatory')

        medias_data = validated_data.pop('medias')
        arr = []
        for media in medias_data:
            if ('id' in media):
                instance_media = MediaPresentation.objects.get(id=media['id'])
                instance_media.type = media['type']
                instance_media.mediaUrl = media['mediaUrl']
                instance_media.save()
                n = instance_media
            else:
                if (len(MediaPresentation.objects.all()) == 0):
                    media['id'] = 1
                else:
                    media['id'] = MediaPresentation.objects.all().latest('id').id + 1
                n = MediaPresentation.objects.create(**media)
            arr.append(n.id)

        instance.medias = arr
        instance.save()

        return instance


class TaskInterventionSerializer(serializers.ModelSerializer):
    medias = MediaPresentationSerializer(many=True)
    parameters = JSONSerializerField()

    class Meta:
        model = TaskIntervention
        fields = ('id', 'type', 'statement', 'medias',
                  'orderPosition', 'first', 'next', 'obligatory',
                  'appPackage', 'parameters'
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
            validated_data['id'] = Intervention.objects.all().latest('id').id + 1

        medias_data = validated_data.pop('medias')
        arr = []
        for media_data in medias_data:
            if (len(MediaPresentation.objects.all()) == 0):
                media_data['id'] = 1
            else:
                media_data['id'] = MediaPresentation.objects.all().latest('id').id + 1
            n = MediaPresentation.objects.create(**media_data)
            arr.append(n.id)
        # validated_data['medias'] = arr

        intervention = TaskIntervention.objects.create(**validated_data)
        intervention.medias = arr
        intervention.save()
        return intervention

    def update(self, instance, validated_data):

        instance.statement = validated_data.get('statement')
        instance.orderPosition = validated_data.get('orderPosition')
        instance.first = validated_data.get('first')
        instance.next = validated_data.get('next')
        instance.obligatory = validated_data.get('obligatory')
        instance.appPackage = validated_data.get('appPackage')
        instance.parameters = validated_data.get('parameters')

        medias_data = validated_data.pop('medias')
        arr = []
        for media in medias_data:
            if ('id' in media):
                instance_media = MediaPresentation.objects.get(id=media['id'])
                instance_media.type = media['type']
                instance_media.mediaUrl = media['mediaUrl']
                instance_media.save()
                n = instance_media
            else:
                if (len(MediaPresentation.objects.all()) == 0):
                    media['id'] = 1
                else:
                    media['id'] = MediaPresentation.objects.all().latest('id').id + 1
                n = MediaPresentation.objects.create(**media)
            arr.append(n.id)

        instance.medias = arr
        instance.save()

        return instance


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
            validated_data['id'] = Intervention.objects.all().latest('id').id + 1

        medias_data = validated_data.pop('medias')
        arr = []
        for media_data in medias_data:
            if (len(MediaPresentation.objects.all()) == 0):
                media_data['id'] = 1
            else:
                media_data['id'] = MediaPresentation.objects.all().latest('id').id + 1
            n = MediaPresentation.objects.create(**media_data)
            arr.append(n.id)
        # validated_data['medias'] = arr

        intervention = MediaIntervention.objects.create(**validated_data)
        intervention.medias = arr
        intervention.save()
        return intervention

    def update(self, instance, validated_data):

        instance.statement = validated_data.get('statement')
        instance.orderPosition = validated_data.get('orderPosition')
        instance.first = validated_data.get('first')
        instance.next = validated_data.get('next')
        instance.obligatory = validated_data.get('obligatory')
        instance.mediaType = validated_data.get('mediaType')

        medias_data = validated_data.pop('medias')
        arr = []
        for media in medias_data:
            if ('id' in media):
                instance_media = MediaPresentation.objects.get(id=media['id'])
                instance_media.type = media['type']
                instance_media.mediaUrl = media['mediaUrl']
                instance_media.save()
                n = instance_media
            else:
                if (len(MediaPresentation.objects.all()) == 0):
                    media['id'] = 1
                else:
                    media['id'] = MediaPresentation.objects.all().latest('id').id + 1
                n = MediaPresentation.objects.create(**media)
            arr.append(n.id)

        instance.medias = arr
        instance.save()

        return instance


class QuestionInterventionSerializer(serializers.ModelSerializer):
    medias = MediaPresentationSerializer(many=True)
    complexConditions = ComplexConditionSerializer(many=True)
    options = JSONSerializerField()
    conditions = JSONSerializerField()

    class Meta:
        model = QuestionIntervention
        fields = ('id', 'type', 'statement', 'medias',
                  'orderPosition', 'first', 'next', 'obligatory', 'questionType', 'options', 'conditions',
                  'complexConditions'
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
            validated_data['id'] = Intervention.objects.all().latest('id').id + 1

        medias_data = validated_data.pop('medias')
        complex_cond_data = validated_data.pop('complexConditions')
        print complex_cond_data

        arr_medias = []
        arr_compl = []

        intervention = QuestionIntervention.objects.create(**validated_data)

        for media_data in medias_data:
            if (len(MediaPresentation.objects.all()) == 0):
                media_data['id'] = 1
            else:
                media_data['id'] = MediaPresentation.objects.all().latest('id').id + 1

            n = MediaPresentation.objects.create(**media_data)
            arr_medias.append(n.id)

        for cc in complex_cond_data:
            n = ComplexCondition.objects.create(**cc)
            arr_compl.append(n.id)

        intervention.medias = arr_medias
        intervention.complexConditions = arr_compl

        intervention.save()
        return intervention

    def update(self, instance, validated_data):

        instance.statement = validated_data.get('statement')
        instance.orderPosition = validated_data.get('orderPosition')
        instance.first = validated_data.get('first')
        instance.next = validated_data.get('next')
        instance.obligatory = validated_data.get('obligatory')
        instance.mediaType = validated_data.get('mediaType')
        instance.questionType = validated_data.get('questionType')
        instance.options = validated_data.get('options')
        instance.conditions = validated_data.get('conditions')

        complex_cond_data = validated_data.pop('complexConditions')
        medias_data = validated_data.pop('medias')

        arr_compl = []

        for cc in complex_cond_data:
            n = ComplexCondition.objects.create(**cc)
            arr_compl.append(n.id)

        arr = []
        for media in medias_data:
            if ('id' in media):
                instance_media = MediaPresentation.objects.get(id=media['id'])
                instance_media.type = media['type']
                instance_media.mediaUrl = media['mediaUrl']
                instance_media.save()
                n = instance_media
            else:
                if (len(MediaPresentation.objects.all()) == 0):
                    media['id'] = 1
                else:
                    media['id'] = MediaPresentation.objects.all().latest('id').id + 1
                n = MediaPresentation.objects.create(**media)
            arr.append(n.id)

        instance.medias = arr
        instance.complexConditions = arr_compl
        instance.save()

        return instance
