from django.test import TestCase
from schueler.models import schueler, gast, sitzungssummary
from views import SitzungssummaryViewSet

# class TestCase(TestCase):
#     def setUp(self):
#         schueler.objects.create(ID=40, interventiongroup=0)
#         sitzungssummary.objects.create(ID=20, Art='LB')

#     def test_interventiongroup(self):
#         SitzungssummaryViewSet.getInterventiongroup(20)
#         schuelers = schueler.objects.get(ID=20)
#         self.assertEqual(SitzungssummaryViewSet.getInterventiongroup(20), '0')
