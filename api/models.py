from django.db import models

class Lieu(models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return self.nom


class Discipline(models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return self.nom