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

    :ivar description: Description de l'événement
    :type description: str
    :ivar lieu: Lieu où se déroule l'événement
    :type lieu: Lieu
    :ivar date: Date de l'événement
    :type date: date
    :ivar horraire: Heure de début de l'événement
    :type horraire: time
    :ivar nb_place_total: Nombre total de places disponibles
    :type nb_place_total: int
    :ivar nb_place_restante: Nombre de places encore disponibles
    :type nb_place_restante: int or None
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

        :return: La description de l'événement
        :rtype: str
        """
        return self.description

    def save(self, *args, **kwargs):
        """
        Sauvegarde l'événement avec initialisation automatique des places restantes.

        Lors de la création d'un nouvel événement, si le nombre de places restantes
        n'est pas spécifié, il est automatiquement initialisé avec le nombre total de places.

        :param args: Arguments positionnels pour la méthode save
        :type args: tuple
        :param kwargs: Arguments nommés pour la méthode save
        :type kwargs: dict
        """
        if not self.pk:  # création
            if self.nb_place_restante is None:
                self.nb_place_restante = self.nb_place_total
        super().save(*args, **kwargs)

    class Meta:
        """
        Métadonnées du modèle Evenement.

        :cvar verbose_name: Nom lisible de l'événement au singulier
        :type verbose_name: str
        :cvar verbose_name_plural: Nom lisible de l'événement au pluriel
        :type verbose_name_plural: str
        :cvar ordering: Ordre par défaut pour les requêtes
        :type ordering: list
        """
        verbose_name = "Événement"
        verbose_name_plural = "Événements"
        ordering = ['date', 'horraire']
