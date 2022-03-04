# from django.test import TestCase
# from django.test.utils import setup_test_environment
# from .models import schueler, gast, sitzungssummary
# from .views import SitzungssummaryViewSet

# class TestCase(TestCase):

#      def setUpTestData(cls):
#          print("setUpTestData: Run once to set up non-modified data for all class methods.")
#          pass

#      def setUp(self):
#          print(self)
#          print("setUp: Run once for every test method to setup clean data.")
#          pass
#          # Schüler mit einer vorhandenen Interventiongroup
#          #sitzungssummary.objects.create(ID=155, Art='LB')
#          #sitzungssummary.objects.create(ID=20, Art='LB')
#          #sitzungssummary.objects.create(ID=20, Art='LB')

#          #
#          #schueler.objects.create(ID=40, interventiongroup=0)
#          #schueler.objects.create(ID=40, interventiongroup=0)
#          #schueler.objects.create(ID=40, interventiongroup=0)

#      def test_interventiongroup(self):
#          #SitzungssummaryViewSet.getInterventiongroup(155)
#          #schuelers = schueler.objects.get(ID=20)
#          #self.assertEqual(SitzungssummaryViewSet.getInterventiongroup(155), '0')
#          pass