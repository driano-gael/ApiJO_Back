from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from users.managers import UserManager
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):
    """
    Modèle d'utilisateur personnalisé basé sur l'email.

    Utilise l'email comme identifiant unique et introduit un système de rôles
    pour distinguer les clients, employés et administrateurs.

    :ivar email: Adresse email unique servant d'identifiant
    :vartype email: str
    :ivar role: Rôle de l'utilisateur (client, admin, employe)
    :vartype role: str
    :ivar is_active: Statut actif de l'utilisateur
    :vartype is_active: bool
    :ivar is_staff: Accès à l'interface d'administration Django
    :vartype is_staff: bool
    :ivar date_joined: Date de création du compte
    :vartype date_joined: datetime
    """

    ROLE_CHOICES = (
        ('client', 'Client'),
        ('admin', 'Admin'),
        ('employe', 'Employé'),
    )

    email = models.EmailField(
        unique=True,
        db_index=True,
        help_text="Adresse email unique servant d'identifiant"
    )
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default="client",
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
    date_joined = models.DateTimeField(
        default=timezone.now,
        help_text="Date de création du compte"
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def has_admin_access(self) -> bool:
        """
        Vérifie si l'utilisateur a des privilèges d'administrateur.

        :return: True si l'utilisateur est staff ou a le rôle admin
        :rtype: bool
        """
        return self.is_staff or self.role == 'admin'

    def get_full_name(self) -> str:
        """
        Retourne le nom complet de l'utilisateur.

        :return: Le nom complet s'il existe, sinon l'email
        :rtype: str
        """
        return getattr(self, "nom", None) and getattr(self, "prenom", None) or self.email

    def get_short_name(self) -> str:
        """
        Retourne un nom court de l'utilisateur.

        :return: Le prénom s'il existe, sinon l'email
        :rtype: str
        """
        return getattr(self, "prenom", None) or self.email

    def __str__(self) -> str:
        """
        Représentation textuelle de l'utilisateur.

        :return: L'adresse email de l'utilisateur
        :rtype: str
        """
        return self.email

    class Meta:
        """
        Métadonnées du modèle User.

        :cvar verbose_name: Nom lisible au singulier
        :vartype verbose_name: str
        :cvar verbose_name_plural: Nom lisible au pluriel
        :vartype verbose_name_plural: str
        :cvar ordering: Ordre par défaut des utilisateurs
        :vartype ordering: list
        """
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"
        ordering = ["email"]
