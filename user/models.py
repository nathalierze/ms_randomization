from django.db import models

class User(models.Model):
    id = models.CharField(max_length=200, primary_key=True)