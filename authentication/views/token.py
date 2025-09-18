"""
Vues personnalisées pour l'authentification JWT.

Ce module contient les vues pour l'obtention des tokens JWT
avec des informations supplémentaires sur l'utilisateur.
"""

from rest_framework_simplejwt.views import TokenObtainPairView

from authentication.serializers.token import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Vue personnalisée pour l'obtention des tokens JWT.

    Étend la vue JWT standard pour retourner des informations
    supplémentaires sur l'utilisateur (rôle, email) lors de la connexion.

    Methods:
        POST: Authentifier un utilisateur et retourner les tokens avec infos utilisateur

    Returns:
        - access: Token d'accès JWT
        - refresh: Token de rafraîchissement JWT
        - role: Rôle de l'utilisateur (client, employe, admin)
        - email: Email de l'utilisateur authentifié
    """

    serializer_class = CustomTokenObtainPairSerializer
