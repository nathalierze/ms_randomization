from django.test import TestCase
from django.test.utils import setup_test_environment
from .models import sitzungssummary, schueler, gast
from .views import SitzungssummaryViewSet
from rest_framework.test import APIRequestFactory

class TestCase(TestCase):
    
    # def setUpTestData(self):
        # print("setUpTestData: Run once to set up non-modified data for all class methods.")
        # pass

    # def setUp(self):
        # print("setUp: Run once for every test method to setup clean data.")
        # pass

    # User hat bereits eine Interventiongroup - Funktion soll vorhandene Id zurückgeben
    def test_vorhandene_interventiongroup(self):
        print()
        # Sitzung mit vorhandener Interventiongroup
        sitzungsId = 154
        test_sitzung = sitzungssummary.objects.get(pk=sitzungsId)
        test_schueler = schueler.objects.get(pk=test_sitzung.UserID)
        print(test_schueler.interventiongroup)
        # Testergebnis erwartet: vorhandene Interventiongroup (5)
        interventiongroup_soll = test_schueler.interventiongroup
        # Get-Request für Funktion getInterventiongroup erzeugen - PK = Sitzungs-ID
        request = APIRequestFactory().get("")
        method = SitzungssummaryViewSet.as_view({'get': 'get_interventiongroup'})
        response = method(request, pk=sitzungsId)
        # Testergebnis ist: Response data
        interventiongroup_ist = response.data['interventiongroup']
        print(interventiongroup_ist)
        # Erwartet: interventiongroup_ist = interventiongroup_soll
        self.assertEqual(interventiongroup_ist, interventiongroup_soll)

    # User hat bereits Interventiongroup - Session-Parameter IsExperiment muss auf True gesetzt werden
    def test_isExperiment(self):
        print()
        # IsExperiment = False
        sitzungsId = 155
        test_sitzung = sitzungssummary.objects.get(pk=sitzungsId)
        print(test_sitzung.isExperiment)
        # Get-Request für Funktion getInterventiongroup erzeugen - PK = Sitzungs-ID
        request = APIRequestFactory().get("")
        method = SitzungssummaryViewSet.as_view({'get': 'get_interventiongroup'})
        response = method(request, pk=sitzungsId)
        # Wert von IsExperiment nach dem Request
        isExperiment = sitzungssummary.objects.get(pk=sitzungsId).isExperiment
        print(isExperiment)
        # Erwartet: isExperiment = 1
        self.assertEqual(isExperiment, 1)
 
    # User gehört noch keiner Gruppe an, Sitzungsart != GK
    def test_keine_GK_uebung(self):
        print()
        sitzungsId = 156
        test_sitzung = sitzungssummary.objects.get(pk=sitzungsId)
        test_schueler = schueler.objects.get(pk=test_sitzung.UserID)
        print(test_schueler.interventiongroup)
        # Get-Request für Funktion getInterventiongroup erzeugen - PK = Sitzungs-ID
        request = APIRequestFactory().get("")
        method = SitzungssummaryViewSet.as_view({'get': 'get_interventiongroup'})
        response = method(request, pk=sitzungsId)
        # Testergebnis ist: Response data
        interventiongroup_ist = response.data['interventiongroup']
        print(interventiongroup_ist)
        # Erwartet: interventiongroup_ist = 0
        self.assertEqual(interventiongroup_ist, '0')

    # User gehört noch keiner Gruppe an, Sitzungsart = GK
    def test_neue_interventiongroup_zuordnen(self):
        print()
        sitzungsId = 157
        test_sitzung = sitzungssummary.objects.get(pk=sitzungsId)
        test_schueler = schueler.objects.get(pk=test_sitzung.UserID)
        print(test_schueler.interventiongroup)
        # Get-Request für Funktion getInterventiongroup erzeugen - PK = Sitzungs-ID
        request = APIRequestFactory().get("")
        method = SitzungssummaryViewSet.as_view({'get': 'get_interventiongroup'})
        response = method(request, pk=sitzungsId)
        # Testergebnis ist: Response data
        interventiongroup_ist = response.data['interventiongroup']
        print(interventiongroup_ist)
        # Interventiongroup_ist muss in der Range 1-6 liegen
        groups = ['1', '2', '3', '4', '5', '6']
        is_assigned = interventiongroup_ist in groups
        self.assertEqual(is_assigned, True)

