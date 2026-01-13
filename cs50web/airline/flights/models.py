from django.db import models

# Create your models here.
    #model for flights
class Flight(models.Model):
    origin = models.CharField(max_length=64)      
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    def __str__(slef):
        return f"{self.id}: {self.origin} to {self.destination}"