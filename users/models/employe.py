"""
Modèle de profil employé.

Ce module définit le profil employé qui étend les informations de base
de l'utilisateur avec des données spécifiques aux employés.
"""

from django.db import models
from .base_user import User

class EmployeProfile(models.Model):
    """
    Profil employé lié à un utilisateur.

    Étend les informations de base d'un utilisateur avec des données
    spécifiques aux employés : nom, prénom, matricule et identifiant
    téléphonique professionnel.

    Attributes:
        user (User): Relation one-to-one avec l'utilisateur de base
        nom (str): Nom de famille de l'employé
        prenom (str): Prénom de l'employé
        matricule (str): Numéro de matricule unique de l'employé
        identifiant_telephone (str): Identifiant téléphonique professionnel
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='employe_profile',
        help_text="Utilisateur associé à ce profil employé"
    )
    nom = models.CharField(max_length=100, help_text="Nom de famille de l'employé")
    prenom = models.CharField(max_length=100, help_text="Prénom de l'employé")
    matricule = models.CharField(
        max_length=50,
        unique=True,
        help_text="Numéro de matricule unique de l'employé"
    )
    identifiant_telephone = models.CharField(
        max_length=255,
        help_text="Identifiant téléphonique professionnel"
    )

    def __str__(self):
        """
        Représentation textuelle du profil employé.

        Returns:
            str: Nom complet de l'employé avec matricule
        """
        return f"{self.nom} {self.prenom} ({self.matricule})"

    class Meta:
        """Métadonnées du modèle EmployeProfile."""
        verbose_name = "Profil Employé"
        verbose_name_plural = "Profils Employés"
        ordering = ['nom', 'prenom']
