from django.test import TestCase
from django.test.utils import setup_test_environment
from .models import sitzungssummary, schueler, gast
from .views import SitzungssummaryViewSet
from rest_framework.test import APIRequestFactory


class TestCase(TestCase):
    def test_vorhandene_interventiongroup(self):
        """
        User is already assigned to an intervention group
        check if the intervention groups stays the same
        """
        sitzungsId = 154
        test_sitzung = sitzungssummary.objects.get(pk=sitzungsId)
        test_schueler = schueler.objects.get(pk=test_sitzung.UserID)
        interventiongroup_soll = test_schueler.interventiongroup
        request = APIRequestFactory().get("")
        method = SitzungssummaryViewSet.as_view({"get": "get_interventiongroup"})
        response = method(request, pk=sitzungsId)
        interventiongroup_ist = response.data["interventiongroup"]
        self.assertEqual(interventiongroup_ist, interventiongroup_soll)

    def test_isExperiment(self):
        """
        User is already assigned to an intervention group
        check if is experiment is set true
        """
        sitzungsId = 155
        test_sitzung = sitzungssummary.objects.get(pk=sitzungsId)
        request = APIRequestFactory().get("")
        method = SitzungssummaryViewSet.as_view({"get": "get_interventiongroup"})
        response = method(request, pk=sitzungsId)
        isExperiment = sitzungssummary.objects.get(pk=sitzungsId).isExperiment
        self.assertEqual(isExperiment, 1)

    def test_keine_GK_uebung(self):
        """
        User has no intervention group and type of exercise is not included in the experiment
        intervention group should be set to 0
        """
        sitzungsId = 8
        test_sitzung = sitzungssummary.objects.get(pk=sitzungsId)
        test_schueler = schueler.objects.get(pk=test_sitzung.UserID)
        request = APIRequestFactory().get("")
        method = SitzungssummaryViewSet.as_view({"get": "get_interventiongroup"})
        response = method(request, pk=sitzungsId)
        interventiongroup_ist = response.data["interventiongroup"]
        self.assertEqual(interventiongroup_ist, "0")

    def test_neue_interventiongroup_zuordnen(self):
        """
        User has no interventiongroup and type of exercise is included in the experiment
        """
        sitzungsId = 157
        test_sitzung = sitzungssummary.objects.get(pk=sitzungsId)
        test_schueler = schueler.objects.get(pk=test_sitzung.UserID)
        request = APIRequestFactory().get("")
        method = SitzungssummaryViewSet.as_view({"get": "get_interventiongroup"})
        response = method(request, pk=sitzungsId)
        interventiongroup_ist = response.data["interventiongroup"]
        groups = ["1", "2", "3", "4", "5", "6"]
        is_assigned = interventiongroup_ist in groups
        self.assertEqual(is_assigned, True)
