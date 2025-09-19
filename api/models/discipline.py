"""
Module contenant le modèle Discipline pour la gestion des disciplines sportives.

Ce module définit la structure de données pour les disciplines sportives
dans le cadre des Jeux Olympiques.
"""

from django.db import models

class Discipline(models.Model):
    """
    Modèle représentant une discipline sportive.

    Une discipline est une catégorie de sport (par exemple : natation, athlétisme, etc.)
    qui peut contenir plusieurs épreuves.

    :ivar nom: (str) Nom de la discipline sportive
    :ivar icone: (str) Chemin ou nom de l'icône représentant la discipline
    :ivar epreuves: (Epreuve[]) Liste des épreuves associées
    """
    nom = models.CharField(
        max_length=100,
        help_text="Nom de la discipline sportive"
    )
    icone = models.CharField(
        max_length=200,
        default="",
        help_text="Chemin ou nom de l'icône de la discipline"
    )

    def __str__(self):
        """
        Représentation textuelle de la discipline.

        :return: Le nom de la discipline
        :rtype: str
        """
        return self.nom

    class Meta:
        """
        Métadonnées du modèle Discipline.

        :cvar verbose_name: Nom lisible de la discipline au singulier
        :type verbose_name: str
        :cvar verbose_name_plural: Nom lisible de la discipline au pluriel
        :type verbose_name_plural: str
        :cvar ordering: Ordre par défaut pour les requêtes
        :type ordering: list
        """
        verbose_name = "Discipline"
        verbose_name_plural = "Disciplines"
        ordering = ['nom']

