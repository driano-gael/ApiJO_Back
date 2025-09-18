"""
Module contenant le modèle Evenement pour la gestion des événements sportifs.

Ce module définit la structure de données pour les événements qui se déroulent
lors des Jeux Olympiques, incluant la gestion automatique des places restantes.
"""

from django.db import models
from api.models.lieu import Lieu


class Evenement(models.Model):
    """
    Modèle représentant un événement sportif.

    Un événement est une session sportive qui se déroule à un lieu et à une heure précise,
    avec un nombre de places limité pour les spectateurs.

    Attributes:
        description (str): Description de l'événement (max 250 caractères)
        lieu (Lieu): Lieu où se déroule l'événement (clé étrangère)
        date (date): Date de l'événement
        horraire (time): Heure de début de l'événement
        nb_place_total (int): Nombre total de places disponibles (défaut: 1000)
        nb_place_restante (int): Nombre de places encore disponibles
    """
    description = models.CharField(max_length=250, help_text="Description de l'événement")
    lieu = models.ForeignKey(
        Lieu,
        on_delete=models.CASCADE,
        related_name='evenements',
        help_text="Lieu où se déroule l'événement"
    )
    date = models.DateField(help_text="Date de l'événement")
    horraire = models.TimeField(help_text="Heure de début de l'événement")
    nb_place_total = models.IntegerField(
        default=1000,
        help_text="Nombre total de places disponibles"
    )
    nb_place_restante = models.IntegerField(
        null=True,
        blank=True,
        help_text="Nombre de places encore disponibles"
    )

    def __str__(self):
        """
        Représentation textuelle de l'événement.

        Returns:
            str: La description de l'événement
        """
        return self.description

    def save(self, *args, **kwargs):
        """
        Sauvegarde l'événement avec initialisation automatique des places restantes.

        Lors de la création d'un nouvel événement, si le nombre de places restantes
        n'est pas spécifié, il est automatiquement initialisé avec le nombre total de places.

        Args:
            *args: Arguments positionnels pour la méthode save
            **kwargs: Arguments nommés pour la méthode save
        """
        if not self.pk:  # création
            if self.nb_place_restante is None:
                self.nb_place_restante = self.nb_place_total
        super().save(*args, **kwargs)

    class Meta:
        """Métadonnées du modèle Evenement."""
        verbose_name = "Événement"
        verbose_name_plural = "Événements"
        ordering = ['date', 'horraire']
