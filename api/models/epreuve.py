from django.db import models
from api.models.discipline import Discipline
from api.models.evenement import Evenement


class Epreuve(models.Model):
    libelle = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, default="mixte")
    tour = models.CharField(max_length=100, default="")
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='epreuves')
    evenement = models.ForeignKey(Evenement, on_delete=models.SET_NULL, related_name='epreuves', null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['libelle', 'genre', 'discipline', 'evenement'], name='unique_epreuve_par_discipline_genre_et_evenement')
        ]

    def __str__(self):
        return self.libelle
