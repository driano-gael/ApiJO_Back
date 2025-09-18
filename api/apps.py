"""
Configuration de l'application API des Jeux Olympiques.

Ce module définit la configuration Django pour l'application API
qui gère toutes les entités liées aux Jeux Olympiques.
"""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """
    Configuration de l'application API.

    Définit les paramètres de configuration pour l'application Django
    gérant l'API des Jeux Olympiques (lieux, disciplines, épreuves,
    événements et offres).
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
