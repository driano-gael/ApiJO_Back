"""
Module contenant le modèle Offre pour la gestion des offres commerciales.

Ce module définit la structure de données pour les offres de billets
et packages disponibles pour les événements des Jeux Olympiques.
"""

from django.db import models

class Offre(models.Model):
    """
    Modèle représentant une offre commerciale.

    Une offre correspond à un package ou type de billet disponible
    pour les spectateurs, avec un prix variable selon le nombre de personnes.

    :ivar libelle: Nom de l'offre
    :type libelle: str
    :ivar nb_personne: Nombre de personnes concernées par l'offre
    :type nb_personne: int
    :ivar montant: Montant de l'offre en euros
    :type montant: float
    :ivar description: Description détaillée de l'offre
    :type description: str
    """
    libelle = models.CharField(max_length=100, help_text="Nom de l'offre")
    nb_personne = models.IntegerField(
        default=0,
        help_text="Nombre de personnes concernées par l'offre"
    )
    montant = models.FloatField(
        default=0.00,
        help_text="Montant de l'offre en euros"
    )
    description = models.TextField(
        default="",
        help_text="Description détaillée de l'offre"
    )

    def __str__(self):
        """
        Représentation textuelle de l'offre.

        :return: Le libellé de l'offre
        :rtype: str
        """
        return self.libelle

    class Meta:
        """
        Métadonnées du modèle Offre.

        :cvar verbose_name: Nom lisible de l'offre au singulier
        :type verbose_name: str
        :cvar verbose_name_plural: Nom lisible de l'offre au pluriel
        :type verbose_name_plural: str
        :cvar ordering: Ordre par défaut pour les requêtes
        :type ordering: list
        """
        verbose_name = "Offre"
        verbose_name_plural = "Offres"
        ordering = ['nb_personne', 'montant']
