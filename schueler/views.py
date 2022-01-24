from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import schueler
from .serializers import schuelerSerializer
import random
from rest_framework import generics



# class SchuelerViewSet(viewsets.ModelViewSet):
#     def list(self, request):
#         schuelers = schueler.objects.all()
#         serializer = schuelerSerializer(schuelers, many=True)
#         return Response(serializer.data)

class SchuelerViewSet(generics.ListCreateAPIView):
    queryset = schueler.objects.all()
    serializer_class = schuelerSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = schuelerSerializer(queryset, many=True)
        return Response(serializer.data)