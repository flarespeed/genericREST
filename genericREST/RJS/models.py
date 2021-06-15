from django.db import models

class RandomJson(models.Model):
    storedJSON = models.JSONField()
    deletionTime = models.DateTimeField()