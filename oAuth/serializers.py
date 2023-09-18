from oAuth.models import NewUser
# from oAuth.models import Book
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewUser
        fields = ['url', 'username', 'email', 'is_staff']


# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ['id', 'name', 'author', 'is_delete']
