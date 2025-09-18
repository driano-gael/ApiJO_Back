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

    Attributes:
        libelle (str): Nom de l'offre (max 100 caractères)
        nb_personne (int): Nombre de personnes concernées par l'offre (défaut: 0)
        montant (float): Montant de l'offre en euros (défaut: 0.00)
        description (str): Description détaillée de l'offre
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

        Returns:
            str: Le libellé de l'offre
        """
        return self.libelle

    class Meta:
        """Métadonnées du modèle Offre."""
        verbose_name = "Offre"
        verbose_name_plural = "Offres"
        ordering = ['nb_personne', 'montant']
