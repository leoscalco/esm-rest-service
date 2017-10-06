# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from sensor_section.models import Sensor

class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        # fields = ('id', 'sensor_type', 'sensor')
        fields = ('id', 'sensorType', 'sensor', 'SENSOR_TYPE_INTERVAL',
            'SENSOR_TYPE_TASK'
            )
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }

    def create(self, validated_data):
        if len(Sensor.objects.all()) == 0:
            validated_data['id'] = 1
        else:
            validated_data['id'] = (Sensor.objects.all().latest('id').id) + 1

        p = Sensor.objects.create(**validated_data)

        return p

    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=200)
    # email = serializers.EmailField(required=True)

    # def create(self, validated_data):
    #     """
    #     Create and return a new 'Person' instance, given a validated_data
    #     """
    #     return Person.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing 'PERSON' instance
    #     """
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.email = validated_data.get('email', instance.email)

    #     instance.save()
    #     return instance