from django.db import models

class RandomJson(models.Model):
    storedJSON = models.CharField(max_length=1000)
    deletionTime = models.DateTimeField()

class LinkedDescriptor(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Image(models.Model):
    imageUrl = models.CharField(max_length=2048)
    descriptors = models.ManyToManyField(LinkedDescriptor)