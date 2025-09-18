"""
Gestionnaire personnalisé pour le modèle User.

Ce module définit un gestionnaire personnalisé qui remplace le gestionnaire
par défaut de Django pour gérer les utilisateurs avec email comme identifiant.
"""

from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    """
    Gestionnaire personnalisé pour le modèle User.

    Fournit des méthodes pour créer des utilisateurs avec différents rôles
    en utilisant l'email comme identifiant unique au lieu du username.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Crée et sauvegarde un utilisateur avec l'email et le mot de passe donnés.

        Args:
            email (str): L'adresse email de l'utilisateur
            password (str, optional): Le mot de passe de l'utilisateur
            **extra_fields: Champs supplémentaires pour l'utilisateur

        Returns:
            User: L'utilisateur créé

        Raises:
            ValueError: Si l'email n'est pas fourni
        """
        if not email:
            raise ValueError("L'email est obligatoire")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_admin(self, email, password=None, **extra_fields):
        """
        Crée un utilisateur avec le rôle admin.

        Args:
            email (str): L'adresse email de l'administrateur
            password (str, optional): Le mot de passe de l'administrateur
            **extra_fields: Champs supplémentaires pour l'utilisateur

        Returns:
            User: L'administrateur créé

        Raises:
            ValueError: Si l'email n'est pas fourni
        """
        if not email:
            raise ValueError("L'email est obligatoire")
        extra_fields.setdefault('role', 'admin')
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self.create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Crée un superutilisateur avec tous les privilèges.

        Args:
            email (str): L'adresse email du superutilisateur
            password (str, optional): Le mot de passe du superutilisateur
            **extra_fields: Champs supplémentaires pour l'utilisateur

        Returns:
            User: Le superutilisateur créé
        """
        extra_fields.setdefault('role', 'admin')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)