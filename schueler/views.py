from copyreg import pickle
from django.shortcuts import render
from rest_framework import viewsets, status, permissions, authentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import schueler, sitzungssummary, gast
from .serializers import (
    InterventiongroupSerializer,
    SchuelerSerializer,
    SitzungssummarySerializer,
)
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
    API endpoint to get the users' intervention group
    """

    queryset = sitzungssummary.objects.all()
    serializer_class = SchuelerSerializer
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_interventiongroup(self, request, pk):
        """
        Get interventiongroup from AufgabenID sent
        :return: dictionary with cohort
        """
        try:
            auth = schueler.objects.get(Loginname=request.headers["Username"])

            try:
                sitzung = sitzungssummary.objects.get(pk=pk)

                # config.json defines interventiongroups
                with open("/app/schueler/config.json") as json_file:
                    config_file = json.load(json_file)

                user = schueler.objects.get(pk=sitzung.UserID)
                if user.interventiongroup != "0":
                    cohort = user.interventiongroup
                    if sitzung.Art == "GK":
                        sitzung.isExperiment = True
                        sitzung.save()
                    else:
                        sitzung.isExperiment = False
                        sitzung.save()
                elif sitzung.Art == "GK":
                    user_id = sitzung.UserID
                    user_profile = {}
                    controller = ABTestingController(config_file, user_id, user_profile)
                    cohort = controller.get_cohort("learning_analytics")
                    user.interventiongroup = cohort
                    user.save()
                    sitzung.isExperiment = True
                    sitzung.save()
                else:
                    cohort = "0"
                    user.interventiongroup = 0
                    user.save()

                print("The cohort")
                print(cohort)

                schuelers = schueler.objects.get(ID=user.ID)
                serializer = InterventiongroupSerializer(schuelers)
                sendReport(user.Loginname)
                return Response(serializer.data)

            except:
                cohort_dict = {"interventiongroup": "0"}
                return Response(cohort_dict)

        except schueler.DoesNotExist:
            raise PermissionDenied()
