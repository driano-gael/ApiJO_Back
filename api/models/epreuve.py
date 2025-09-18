"""
Module contenant le modèle Epreuve pour la gestion des épreuves sportives.

Ce module définit la structure de données pour les épreuves sportives,
qui représentent des compétitions spécifiques au sein d'une discipline.
"""

from django.db import models
from api.models.discipline import Discipline
from api.models.evenement import Evenement


class Epreuve(models.Model):
    """
    Modèle représentant une épreuve sportive.

    Une épreuve est une compétition spécifique dans une discipline donnée,
    caractérisée par son genre (homme/femme/mixte) et son tour (finale, qualification, etc.).
    Chaque épreuve est associée à un événement et doit être unique par combinaison
    de critères pour éviter les doublons.

    Attributes:
        libelle (str): Intitulé de l'épreuve (max 100 caractères)
        genre (str): Genre de l'épreuve - homme, femme ou mixte (défaut: "mixte")
        tour (str): Tour de l'épreuve - finale, demi-finale, etc. (max 100 caractères)
        discipline (Discipline): Discipline sportive associée (clé étrangère)
        evenement (Evenement): Événement associé (clé étrangère optionnelle)
    """
    libelle = models.CharField(max_length=100, help_text="Intitulé de l'épreuve")
    genre = models.CharField(
        max_length=100,
        default="mixte",
        help_text="Genre de l'épreuve (homme, femme, mixte)"
    )
    tour = models.CharField(
        max_length=100,
        default="",
        help_text="Tour de l'épreuve (finale, demi-finale, qualification, etc.)"
    )
    discipline = models.ForeignKey(
        Discipline,
        on_delete=models.CASCADE,
        related_name='epreuves',
        help_text="Discipline sportive associée"
    )
    evenement = models.ForeignKey(
        Evenement,
        on_delete=models.SET_NULL,
        related_name='epreuves',
        null=True,
        blank=True,
        help_text="Événement associé à cette épreuve"
    )

    class Meta:
        """Métadonnées du modèle Epreuve."""
        constraints = [
            models.UniqueConstraint(
                fields=['libelle', 'genre', 'discipline', "tour", 'evenement'],
                name='unique_epreuve_par_discipline_genre_tour_et_evenement'
            )
        ]
        verbose_name = "Épreuve"
        verbose_name_plural = "Épreuves"
        ordering = ['discipline__nom', 'genre', 'libelle']

    def __str__(self):
        """
        Représentation textuelle de l'épreuve.

        Returns:
            str: Le libellé de l'épreuve
        """
        return self.libelle
