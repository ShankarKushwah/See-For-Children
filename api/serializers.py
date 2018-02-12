from rest_framework import serializers
from django.contrib.auth import get_user_model
from NGO.models import NGO, Children, Events


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'],
            email=validated_data['email']

        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email')


class ChildrenSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='children_detail_api')

    class Meta:
        model = Children
        fields = ['url', 'id', 'name']


class ChildrenDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Children
        fields = ['id', 'name', 'dob', 'gender', 'school', 'education', 'hobby', 'description', 'video_link', 'image']


class EventSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='event_detail_api')

    class Meta:
        model = Events
        fields = ['url', 'id', 'name']


class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id', 'name', 'type', 'place', 'date', 'image', 'description', 'organizer']


class NGOSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ngo_detail_api')

    class Meta:
        model = NGO
        fields = ['url', 'id', 'name']


class NGODetailSerializer(serializers.ModelSerializer):
    children_set = ChildrenSerializer(many=True)
    events_set = EventSerializer(many=True)

    class Meta:
        model = NGO
        fields = ['id', 'name', 'email', 'established', 'area', 'state', 'city', 'zip_code', 'director', 'image', 'children_set', 'events_set']
