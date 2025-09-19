"""
Fichier principal de configuration des URLs du projet.

Ce module inclut toutes les routes de l'application principale et des applications
secondaires comme l'API et l'authentification.

:module: project.urls
"""

from django.urls import path, include

#: Liste des URL patterns principales du projet
urlpatterns = [
    # API principale des Jeux Olympiques
    path('api/', include('api.urls')),

    # Routes d'authentification (login, logout, registration, token, etc.)
    path('api/auth/', include('authentication.urls')),
]