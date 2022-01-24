import random
from .models import schueler

def grouping(body):
    print("in grouping")
    print(body)

    schueler = schueler.objects.all()

    interventiongroups = ['1','2','3']
    random_num = random.choice(interventiongroups)
    
    return random_num