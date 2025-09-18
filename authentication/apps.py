"""
Configuration de l'application d'authentification.

Ce module définit la configuration Django pour l'application d'authentification
qui gère les utilisateurs, les profils clients/employés et les permissions.
"""

from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    """
    Configuration de l'application d'authentification.

    Définit les paramètres de configuration pour l'application Django
    gérant l'authentification des utilisateurs (clients et employés)
    avec gestion des rôles et permissions.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'
