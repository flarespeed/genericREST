from django.db import models

class RandomJson(models.Model):
    storedJSON = models.CharField(max_length=100000)
    deletionTime = models.DateTimeField()