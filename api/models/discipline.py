from django.db import models

class Discipline(models.Model):
    nom = models.CharField(max_length=100)
    icone = models.CharField(max_length=200, default="")
    def __str__(self):
        return self.nom