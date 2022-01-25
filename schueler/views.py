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
        print(schuelers.last)
        serializer = schuelerSerializer(schuelers, many=True)
        return Response(serializer.data)

    
    def create(self, request):
        serializer = schuelerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def retrieve(self, request, pk=None):
        product = schueler.objects.get(ID=pk)
        serializer = schuelerSerializer(product)
        return Response(serializer.data)

