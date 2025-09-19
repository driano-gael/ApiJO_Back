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

    :ivar user: Relation one-to-one avec l'utilisateur de base
    :vartype user: User
    :ivar nom: Nom de famille du client
    :vartype nom: str
    :ivar prenom: Prénom du client
    :vartype prenom: str
    :ivar telephone: Numéro de téléphone du client
    :vartype telephone: str
    :ivar cle_chiffree: Clé chiffrée générée automatiquement
    :vartype cle_chiffree: str
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

        :param args: Arguments positionnels pour la méthode save
        :param kwargs: Arguments nommés pour la méthode save
        """
        if not self.cle_chiffree:
            raw_key = f"{self.user.email}-{self.nom}"
            self.cle_chiffree = hashlib.sha256(raw_key.encode('utf-8')).hexdigest()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        """
        Représentation textuelle du profil client.

        :return: Nom complet du client (nom + prénom)
        :rtype: str
        """
        return f"{self.nom} {self.prenom}"

    class Meta:
        """
        Métadonnées du modèle ClientProfile.

        :cvar verbose_name: Nom lisible au singulier
        :vartype verbose_name: str
        :cvar verbose_name_plural: Nom lisible au pluriel
        :vartype verbose_name_plural: str
        :cvar ordering: Ordre par défaut (nom, prénom)
        :vartype ordering: list
        """
        verbose_name = "Profil Client"
        verbose_name_plural = "Profils Clients"
        ordering = ['nom', 'prenom']
