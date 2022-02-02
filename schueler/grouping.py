import random
from urllib import request
from .models import schueler, sitzungssummary

from .views import SchuelerViewSet, SitzungssummaryViewSet
import json

def grouping(body):
    sitzung = sitzungssummary.objects.get(pk=body)

    if(sitzung.UserAttribut=='Schüler'):
        user = schueler.objects.get(pk=sitzung.UserID)
    elif(sitzung.UserAttribut=='Gast'):
        print("gast noch nicht implementiert")
    
    # erst checken ob user bereits interventionsgruppe -> dann gruppe zurückgebeb
    # dann checken ob gk -> user gruppe zuordnen
    # wenn nicht gk -> 0 zurückgeben 
    if(user.interventiongroup!='0'):
        cohort = user.interventiongroup
        sitzung.isExperiment = 1
        sitzung.save()
    elif(sitzung.Art=='GK'):
        cohorts = ['1','2','3','4','5']
        cohort = random.choice(cohorts)

        user.interventiongroup = cohort
        user.save()

        sitzung.isExperiment = 1
        sitzung.save()
    else:
        cohort = '0'

    print(cohort)
    return 5