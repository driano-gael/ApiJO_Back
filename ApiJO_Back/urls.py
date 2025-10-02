"""
Fichier principal de configuration des URLs du projet.

Ce module inclut toutes les routes de l'application principale et des applications
secondaires comme l'API et l'authentification.

:module: project.urls
"""

from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

#: Liste des URL patterns principales du projet
urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # API principale des Jeux Olympiques
    path('api/', include('api.urls')),

    # Routes d'authentification (login, logout, registration, token, etc.)
    path('api/auth/', include('authentication.urls')),
    path('api/payment/', include('payment.urls')),
]
