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
    (par exemple : Stade de France, Centre Aquatique, etc.).

    :ivar nom: Nom du lieu sportif
    :type nom: str
    """
    nom = models.CharField(max_length=100, help_text="Nom du lieu sportif")

    def __str__(self):
        """
        Représentation textuelle du lieu.

        :return: Le nom du lieu
        :rtype: str
        """
        return self.nom

    class Meta:
        """
        Métadonnées du modèle Lieu.

        :cvar verbose_name: Nom lisible du lieu au singulier
        :type verbose_name: str
        :cvar verbose_name_plural: Nom lisible du lieu au pluriel
        :type verbose_name_plural: str
        :cvar ordering: Ordre par défaut pour les requêtes
        :type ordering: list
        """
        verbose_name = "Lieu"
        verbose_name_plural = "Lieux"
        ordering = ['nom']
