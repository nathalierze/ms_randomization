from django.db import models

# Create your models here.
# class Meta:
#     db_table = ''

class schueler(models.Model):
    class Meta:
        db_table = 'schueler'
    
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=30, blank=True )
    Passwort_express = models.CharField(max_length=32, blank=True )
    Email = models.CharField(max_length=40, blank=True )
    Loginname = models.CharField(max_length=60, blank=True )
    Passwort = models.IntegerField(blank=True )
    SessionID = models.CharField(max_length=32, blank=True )
    Lehrername = models.CharField(max_length=30, blank=True )
    LehrerID = models.IntegerField(blank=True)
    Klassenname = models.CharField(max_length=30, blank=True )
    Geschlecht = models.CharField(max_length=20, blank=True )
    Klassenstufe = models.CharField(max_length=20, blank=True )
    Anmeldedatum = models.IntegerField(blank=True)
    Anmeldeklassenstufe = models.CharField(max_length=30, blank=True )
    Altklasse = models.CharField(max_length=30, blank=True )
    gesperrt = models.CharField(max_length=30, blank=True )
    Aufgaben = models.CharField(max_length=300, blank=True )
    Altaufgaben = models.CharField(max_length=600, blank=True )
    done = models.IntegerField(blank=True)
    Info = models.CharField(max_length=60, blank=True )
    interventiongroup = models.IntegerField(blank=True)

    