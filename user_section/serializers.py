from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import Observer, Participant, Person

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ObserverContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ('id', 'name', 'email')

class ObserverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Observer
        fields = ('id', 'name', 'email', 'role', 'contacts')

class ObserverVerboseSerializer(serializers.ModelSerializer):
    contacts = ObserverContactsSerializer(many=True)

    class Meta:
        model = Observer
        fields = ('id', 'name', 'email', 'role', 'contacts')

    def create(self, validated_data):
        # contacts_data = validated_data.get('contacts')
        contacts_data = validated_data.pop('contacts')
        participants = []
        for contact in contacts_data:
            # contact['email'] = "forc@email.com"
            participants.append(Participant.objects.create(**contact))

        print participants
        # validated_data['contacts'] = participants

        observer = Observer.objects.create(
            **validated_data
            )

        for p in participants:
            observer.contacts.add(p)

        observer.save()

        return observer

    def update(self, instance, validated_data):
        # print validated_data

        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.role = validated_data.get('role', instance.role)

        contacts_data = validated_data.pop('contacts')

        for i in range(len(contacts_data)):
            p = Participant.objects.get(email=instance.contacts.all()[i].email)
            p.name = contacts_data[i]['name']
            p.email = contacts_data[i]['email']
            p.save()

        instance.save()

        return instance

class ParticipantSerializer(serializers.ModelSerializer):
    # contacts = ContactsSerializer(many=False)

    class Meta:
        model = Participant
        fields = ('id', 'name', 'email',
            # 'observerResponsible'
            )
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