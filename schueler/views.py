from copyreg import pickle
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import schueler, sitzungssummary, gast
from .serializers import interventiongroupSerializer, schuelerSerializer, sitzungssummarySerializer
import random
from rest_framework import generics

from ABTesting import ABTestingController
import json
import os
class SchuelerViewSet(viewsets.ModelViewSet):
    """
    API endpoint
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
        schuelers = schueler.objects.get(ID=pk)
        serializer = schuelerSerializer(schuelers)
        return Response(serializer.data)

    def update(self, request, pk=None):
        schuelers = schueler.objects.get(ID=pk)
        serializer = schuelerSerializer(instance=schuelers, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

class SitzungssummaryViewSet(viewsets.ModelViewSet):
    """
    API endpoint
    """
    queryset = sitzungssummary.objects.all()
    serializer_class = schuelerSerializer

    def list(self, request):
        sitzungssummaries = sitzungssummary.objects.all()
        print(sitzungssummaries.last)
        serializer = sitzungssummarySerializer(sitzungssummaries, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = sitzungssummarySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        sitzungssummaries = sitzungssummary.objects.get(ID=pk)
        serializer = sitzungssummarySerializer(sitzungssummaries)
        return Response(serializer.data)

    def getInterventiongroup(self, request, pk):
        sitzung = sitzungssummary.objects.get(pk=pk)

        print(pk)

        # lade Daten aus config file
        with open('/app/schueler/config.json') as json_file:
            config_file = json.load(json_file)

        if(sitzung.UserAttribut=='Schüler'):
            user = schueler.objects.get(pk=sitzung.UserID)
            print(user.ID)
        elif(sitzung.UserAttribut=='Gast'):
            user = gast.objects.get(pk=sitzung.UserID)
        
        # erst checken ob user bereits interventionsgruppe -> dann gruppe zurückgebeb
        # dann checken ob gk -> user gruppe zuordnen
        # wenn nicht gk -> 0 zurückgeben 
        if(user.interventiongroup!='0'):
            cohort = user.interventiongroup
            sitzung.isExperiment = True
            sitzung.save()

        elif(sitzung.Art=='GK'):
            user_id = sitzung.UserID
            user_profile = {}
            controller = ABTestingController(config_file, user_id, user_profile)
            cohort = controller.get_cohort('learning_analytics')
            
            # alter code
            #cohorts = ['1','2','3','4','5','6']
            #cohort = random.choice(cohorts)

            user.interventiongroup = cohort
            user.save()

            sitzung.isExperiment = True
            sitzung.save()
        else:
            cohort = '0'
            user.interventiongroup = 0
            user.save()

        print(cohort)

        schuelers = schueler.objects.get(ID=user.ID)
        serializer = interventiongroupSerializer(schuelers)

        return Response(serializer.data)

