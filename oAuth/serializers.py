from oAuth.models import NewUser
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewUser
        fields = ['url', 'username', 'email', 'is_staff']
