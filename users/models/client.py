"""
Modèle de profil client.

Ce module définit le profil client qui étend les informations de base
de l'utilisateur avec des données spécifiques aux clients.
"""

import hashlib
from django.db import models
from .base_user import User

class ClientProfile(models.Model):
    """
    Profil client lié à un utilisateur.

    Étend les informations de base d'un utilisateur avec des données
    spécifiques aux clients : nom, prénom, téléphone et clé chiffrée
    générée automatiquement pour la sécurité.

    Attributes:
        user (User): Relation one-to-one avec l'utilisateur de base
        nom (str): Nom de famille du client
        prenom (str): Prénom du client
        telephone (str): Numéro de téléphone du client
        cle_chiffree (str): Clé chiffrée générée automatiquement
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='client_profile',
        help_text="Utilisateur associé à ce profil client"
    )
    nom = models.CharField(max_length=100, help_text="Nom de famille du client")
    prenom = models.CharField(max_length=100, help_text="Prénom du client")
    telephone = models.CharField(max_length=20, help_text="Numéro de téléphone")
    cle_chiffree = models.CharField(
        max_length=255,
        help_text="Clé chiffrée générée automatiquement"
    )

    def save(self, *args, **kwargs):
        """
        Sauvegarde le profil client avec génération automatique de la clé chiffrée.

        Génère automatiquement une clé chiffrée basée sur l'email et le nom
        si elle n'existe pas déjà.

        Args:
            *args: Arguments positionnels pour la méthode save
            **kwargs: Arguments nommés pour la méthode save
        """
        if not self.cle_chiffree:
            raw_key = f"{self.user.email}-{self.nom}"
            self.cle_chiffree = hashlib.sha256(raw_key.encode('utf-8')).hexdigest()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Représentation textuelle du profil client.

        Returns:
            str: Nom complet du client (nom + prénom)
        """
        return f"{self.nom} {self.prenom}"

    class Meta:
        """Métadonnées du modèle ClientProfile."""
        verbose_name = "Profil Client"
        verbose_name_plural = "Profils Clients"
        ordering = ['nom', 'prenom']
