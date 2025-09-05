from django.db import models

class Offre(models.Model):
    libelle = models.CharField(max_length=100)
    nb_personne = models.IntegerField(default=0)
    montant = models.FloatField(default=0.00)
    description = models.TextField(default="")

    def __str__(self):
        return self.libelle
