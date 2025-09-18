"""
Modèle d'utilisateur de base personnalisé.

Ce module définit le modèle User personnalisé qui remplace le modèle par défaut
de Django en utilisant l'email comme identifiant et en ajoutant un système de rôles.
"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from users.managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    """
    Modèle d'utilisateur personnalisé basé sur l'email.

    Remplace le modèle User par défaut de Django pour utiliser l'email
    comme identifiant unique et ajoute un système de rôles pour gérer
    les permissions (client, admin, employé).

    Attributes:
        email (str): Adresse email unique servant d'identifiant
        role (str): Rôle de l'utilisateur (client, admin, employe)
        is_active (bool): Statut actif de l'utilisateur
        is_staff (bool): Accès à l'interface d'administration Django
    """
    ROLE_CHOICES = (
        ('client', 'Client'),
        ('admin', 'Admin'),
        ('employe', 'Employé'),
    )

    email = models.EmailField(unique=True, help_text="Adresse email unique")
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        help_text="Rôle de l'utilisateur dans le système"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Indique si l'utilisateur est actif"
    )
    is_staff = models.BooleanField(
        default=False,
        help_text="Accès à l'interface d'administration Django"
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def has_admin_access(self):
        """
        Vérifie si l'utilisateur a des privilèges d'administrateur.

        Returns:
            bool: True si l'utilisateur est staff ou a le rôle admin
        """
        return self.is_staff or self.role == 'admin'

    def __str__(self):
        """
        Représentation textuelle de l'utilisateur.

        Returns:
            str: L'adresse email de l'utilisateur
        """
        return self.email

    class Meta:
        """Métadonnées du modèle User."""
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"
        ordering = ['email']
