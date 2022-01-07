from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .producer import publish
from .serializers import UserSerializer
import random


class UserAPIView(viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(User, many=True)
        print("get method")
        publish()
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        #publish()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
