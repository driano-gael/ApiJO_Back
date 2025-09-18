"""
Configuration de l'application de gestion des utilisateurs.

Ce module définit la configuration Django pour l'application users
qui gère les modèles d'utilisateurs, profils clients et employés.
"""

from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    Configuration de l'application users.

    Définit les paramètres de configuration pour l'application Django
    gérant les utilisateurs de base, les profils clients et employés
    avec leurs gestionnaires personnalisés.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
