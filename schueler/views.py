from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import schueler
from .serializers import schuelerSerializer
import random
from rest_framework import generics

class SchuelerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = schueler.objects.all()
    serializer_class = schuelerSerializer

    def list(self, request):
        schuelers = schueler.objects.all()
        serializer = schuelerSerializer(schuelers, many=True)
        return Response(serializer.data)


