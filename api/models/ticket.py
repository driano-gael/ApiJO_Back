"""
Module contenant le modèle Ticket pour la gestion des billets.

Ce module définit la structure de données pour les tickets achetés
par les clients pour les événements des Jeux Olympiques.
Chaque ticket est associé à un client, un événement et une offre spécifique,
et possède une clé unique générée automatiquement.
"""

import hashlib
from django.db import models
from users.models import ClientProfile

class Ticket(models.Model):
    """
    Modèle représentant un ticket pour un événement sportif.

    Un ticket est associé à un client, un événement et une offre spécifique.
    Chaque ticket possède un statut et une clé unique générée automatiquement
    pour garantir l'unicité.

    :ivar client: Le client possédant le ticket
    :type client: ClientProfile
    :ivar evenement: L'événement associé au ticket
    :type evenement: Evenement
    :ivar offre: L'offre choisie pour ce ticket
    :type offre: Offre
    :ivar date_achat: Date et heure d'achat du ticket
    :type date_achat: datetime
    :ivar statut: Statut du ticket ('valide' ou 'invalide')
    :type statut: str
    :ivar key: Clé unique générée pour le ticket
    :type key: str
    """
    STATUT_CHOICES = [
        ('valide', 'Valide'),
        ('invalide', 'Invalide')
    ]

    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    evenement = models.ForeignKey('Evenement', on_delete=models.CASCADE)
    offre = models.ForeignKey('Offre', on_delete=models.CASCADE)
    date_achat = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='valide')
    key = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        """
        Sauvegarde le ticket et génère une clé unique incluant l'ID.

        La clé est calculée après la première insertion pour inclure self.id,
        garantissant l'unicité absolue. La clé est un hash SHA-256 basé sur
        le client, la date d'achat et l'identifiant du ticket.
        """
        # Sauvegarde initiale pour générer l'ID si nécessaire
        if not self.id:
            super().save(*args, **kwargs)

        if not self.key:
            raw_key = f"{self.client.cle_chiffree}-{self.date_achat}-{self.id}"
            self.key = hashlib.sha256(raw_key.encode('utf-8')).hexdigest()
            super().save(*args, **kwargs)

    def __str__(self):
        """
        Représentation textuelle du ticket.

        :return: Chaîne décrivant le ticket avec son ID, l'événement et le nom du client
        :rtype: str
        """
        return f"Ticket {self.id} - {self.evenement} - {self.client.nom}"

    class Meta:
        """
        Métadonnées du modèle Ticket.

        :cvar ordering: Ordre par défaut des tickets, triés par date d'achat décroissante
        :type ordering: list
        """
        ordering = ['-date_achat']
