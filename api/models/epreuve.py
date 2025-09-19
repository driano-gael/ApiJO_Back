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
    caractérisée par son genre (homme/femme/mixte) et son tour (finale, demi-finale, etc.).
    Chaque épreuve est associée à un événement et doit être unique par combinaison
    de critères pour éviter les doublons.

    :ivar libelle: Intitulé de l'épreuve
    :type libelle: str
    :ivar genre: Genre de l'épreuve (homme, femme, mixte)
    :type genre: str
    :ivar tour: Tour de l'épreuve (finale, demi-finale, qualification, etc.)
    :type tour: str
    :ivar discipline: Discipline sportive associée
    :type discipline: Discipline
    :ivar evenement: Événement associé à cette épreuve (optionnel)
    :type evenement: Evenement or None
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
        """
        Métadonnées du modèle Epreuve.

        :cvar constraints: Contraintes d'unicité sur libelle, genre, discipline, tour et evenement
        :type constraints: list
        :cvar verbose_name: Nom lisible de l'épreuve au singulier
        :type verbose_name: str
        :cvar verbose_name_plural: Nom lisible de l'épreuve au pluriel
        :type verbose_name_plural: str
        :cvar ordering: Ordre par défaut pour les requêtes
        :type ordering: list
        """
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

        :return: Le libellé de l'épreuve
        :rtype: str
        """
        return self.libelle
