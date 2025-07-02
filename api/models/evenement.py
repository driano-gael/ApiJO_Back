from django.db import models
from api.models.lieu import Lieu


class Evenement(models.Model):
    description = models.CharField(max_length=250)
    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE, related_name='evenements')
    date = models.DateField()
    horraire= models.TimeField()

    def __str__(self):
        return self.description