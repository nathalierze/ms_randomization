from copyreg import pickle
from django.shortcuts import render

# Create your views here
from rest_framework import viewsets, status, permissions, authentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import schueler, sitzungssummary, gast
from .serializers import InterventiongroupSerializer, SchuelerSerializer, SitzungssummarySerializer
import random
from rest_framework import generics
from .calldiagnostic import sendReport
from admin.authentication import TokenAuthentication
from django.core.exceptions import PermissionDenied


from ABTesting import ABTestingController
import json
import os

class SitzungssummaryViewSet(viewsets.ModelViewSet):
    """
    API endpoint
    """
    queryset = sitzungssummary.objects.all()
    serializer_class = SchuelerSerializer
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_interventiongroup(self, request, pk):
        try:
            auth = schueler.objects.get(Loginname = request.headers['Username'])

            sitzung = sitzungssummary.objects.get(pk=pk)

            # lade Daten aus config file
            with open('/app/schueler/config.json') as json_file:
                config_file = json.load(json_file)

            if(sitzung.UserAttribut=='Schüler'):
                user = schueler.objects.get(pk=sitzung.UserID)
            elif(sitzung.UserAttribut=='Gast'):
                user = gast.objects.get(pk=sitzung.UserID)
            
            # erst checken ob user bereits interventionsgruppe -> dann gruppe zurückgebeb
            # dann checken ob gk -> user gruppe zuordnen
            # wenn nicht gk -> 0 zurückgeben 
            if(user.interventiongroup!='0'):
                cohort = user.interventiongroup
                if(sitzung.Art =='GK'):
                    sitzung.isExperiment = True
                    sitzung.save()
                else:
                    sitzung.isExperiment = False
                    sitzung.save()

            elif(sitzung.Art=='GK'):
                user_id = sitzung.UserID
                user_profile = {}
                controller = ABTestingController(config_file, user_id, user_profile)
                cohort = controller.get_cohort('learning_analytics')
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
            serializer = InterventiongroupSerializer(schuelers)

            sendReport(user.Loginname)

            return Response(serializer.data)
            
        except schueler.DoesNotExist:
            raise PermissionDenied() 