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

    Attributes:
        nom (str): Le nom de la discipline sportive (max 100 caractères)
        icone (str): Le chemin ou nom de l'icône représentant la discipline (max 200 caractères)
    """
    nom = models.CharField(max_length=100, help_text="Nom de la discipline sportive")
    icone = models.CharField(
        max_length=200,
        default="",
        help_text="Chemin ou nom de l'icône de la discipline"
    )

    def __str__(self):
        """
        Représentation textuelle de la discipline.

        Returns:
            str: Le nom de la discipline
        """
        return self.nom

    class Meta:
        """Métadonnées du modèle Discipline."""
        verbose_name = "Discipline"
        verbose_name_plural = "Disciplines"
        ordering = ['nom']
