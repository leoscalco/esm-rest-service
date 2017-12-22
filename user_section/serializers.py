from django.contrib.auth.models import User, Group
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import IntegrityError, transaction
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


# class PersonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Person
#         fields = ('id', 'name', 'email')
#         extra_kwargs = {
#             "id": {
#                 "read_only": False,
#                 "required": False,
#             }
#         }

#     def to_interval_value(self, obj):
#         try:
#             obj_ = Observer.objects.get(id=obj['id'])
#         except Observer.objects.DoesNotExist:
#             obj_ = Participant.objects.get(id=obj['id'])

#         if isinstance(obj_, Observer):
#             return ObserverSerializer(context=self.context).to_interval_value(obj)
#         elif isinstance(obj_, Participant):
#             return ParticipantSerializer(context=self.context).to_interval_value(obj)
#         else:
#             return super(PersonSerializer, self).to_interval_value(obj)

class ObserverContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ('id', 'name', 'email')
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
            "email": {
                'validators': [UnicodeUsernameValidator()],
            }
        }


class ObserverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observer
        fields = ('id', 'name', 'email', 'role', 'contacts')
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
            "email": {
                'validators': [UnicodeUsernameValidator()],
            }
        }

    def create(self, validated_data):
        try:
            with transaction.atomic():
                if (len(Person.objects.all()) == 0):
                    validated_data['id'] = 1
                else:
                    validated_data['id'] = Person.objects.all().latest('id').id + 1

                contacts_data = validated_data.pop('contacts')

                participants = []
                for contact in contacts_data:
                    # contact['email'] = "forc@email.com"
                    participants.append(Participant.objects.create(name=contact['name'],
                                                                   email=contact['email']))

                # validated_data['contacts'] = participants

                observer = Observer.objects.create(
                    id=validated_data['id'],
                    name=validated_data['name'],
                    email=validated_data['email'],
                    role=validated_data['role']
                )

                for p in participants:
                    observer.contacts.add(p)

                observer.save()

                return observer
        except IntegrityError:
            return "error"


class ObserverVerboseSerializer(serializers.ModelSerializer):
    contacts = ObserverContactsSerializer(many=True)

    class Meta:
        model = Observer
        fields = ('id', 'name', 'email', 'role', 'contacts')
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
            "email": {
                'validators': [UnicodeUsernameValidator()],
            }
        }

    def create(self, validated_data):
        # contacts_data = validated_data.get('contacts')
        try:
            with transaction.atomic():
                if (len(Person.objects.all()) == 0):
                    validated_data['id'] = 1
                else:
                    validated_data['id'] = Person.objects.all().latest('id').id + 1

                contacts_data = validated_data.pop('contacts')

                participants = []
                for contact in contacts_data:
                    # contact['email'] = "forc@email.com"
                    participants.append(Participant.objects.create(name=contact['name'],
                                                                   email=contact['email']))

                # validated_data['contacts'] = participants

                observer = Observer.objects.create(
                    name=validated_data['name'],
                    email=validated_data['email'],
                    role=validated_data['role']
                )

                for p in participants:
                    observer.contacts.add(p)

                observer.save()

                return observer

        except IntegrityError:
            return "Error"

    def update(self, instance, validated_data):
        # print validated_data
        try:
            with transaction.atomic():
                instance.name = validated_data.get('name', instance.name)
                instance.email = validated_data.get('email', instance.email)
                instance.role = validated_data.get('role', instance.role)

                if 'contacts' in validated_data:
                    contacts_data = validated_data.pop('contacts')
                    for contact in contacts_data:
                        if 'id' in contact:
                            p = Participant.objects.get(
                                id=contact['id']
                            )
                            p.name = contact['name'],
                            p.email = contact['email']
                            p.save()
                        else:
                            p = Participant.objects.create(
                                name=contact['name'], email=contact['email']
                            )
                            p.save()
                        instance.contacts.add(p)

                instance.save()

                return instance
        except IntegrityError:
            return "Error"


class ParticipantSerializer(serializers.ModelSerializer):
    # contacts = ContactsSerializer(many=False)

    class Meta:
        model = Participant
        fields = ('id', 'name', 'email',
            # 'observerResponsible'
                  )
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
            "email": {
                'validators': [UnicodeUsernameValidator()],
            }
        }

    def create(self, validated_data):
        if (len(Person.objects.all()) == 0):
            validated_data['id'] = 1
        else:
            validated_data['id'] = Person.objects.all().latest('id').id + 1

        p = Participant.objects.create(**validated_data)

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
