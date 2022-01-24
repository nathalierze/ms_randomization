from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import schueler
from .serializers import UserSerializer


class SchuelerViewSet(viewsets.ViewSet):
    def list(self, request):
        schueler = schueler.objects.all()
        serializer = UserSerializer(schueler, many=True)
        return Response(serializer.data)