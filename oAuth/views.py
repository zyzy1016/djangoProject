from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from oAuth.serializers import UserSerializer

from oAuth.models import NewUser


class UserInfoViewSet(viewsets.ViewSet):
    queryset = NewUser.objects.all().order_by('-date_joined')
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        print('OK')
        user_info = NewUser.objects.filter(id=request.user.id).values()[0]
        role = request.user.roles
        if role == 0:
            user_info['roles'] = ['admin']
        else:
            user_info['roles'] = ['user']

        return Response(user_info)


class UserViewSet(viewsets.ModelViewSet):
    queryset = NewUser.objects.all()
    serializer_class = UserSerializer
