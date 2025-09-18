"""
Module contenant le modèle Lieu pour la gestion des lieux sportifs.

Ce module définit la structure de données pour les lieux où se déroulent
les événements sportifs des Jeux Olympiques.
"""

from django.db import models

class Lieu(models.Model):
    """
    Modèle représentant un lieu sportif.

    Un lieu est un site où se déroulent les événements sportifs
    (par exemple : Stade de France, Centre Aquatique, etc.)

    Attributes:
        nom (str): Le nom du lieu sportif (max 100 caractères)
    """
    nom = models.CharField(max_length=100, help_text="Nom du lieu sportif")

    def __str__(self):
        """
        Représentation textuelle du lieu.

        Returns:
            str: Le nom du lieu
        """
        return self.nom

    class Meta:
        """Métadonnées du modèle Lieu."""
        verbose_name = "Lieu"
        verbose_name_plural = "Lieux"
        ordering = ['nom']
