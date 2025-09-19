"""
Vues personnalisées pour l'authentification JWT.

Ce module contient les vues pour l'obtention des tokens JWT
avec des informations supplémentaires sur l'utilisateur.

:module: authentication.views.token
"""

from rest_framework_simplejwt.views import TokenObtainPairView
from authentication.serializers.token import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Vue personnalisée pour l'obtention des tokens JWT.

    Étend la vue JWT standard pour retourner des informations
    supplémentaires sur l'utilisateur (rôle, email) lors de la connexion.

    :methods:
        - POST: Authentifier un utilisateur et retourner les tokens avec infos utilisateur

    :returns:
        dict:
            - ``access`` : Token d'accès JWT
            - ``refresh`` : Token de rafraîchissement JWT
            - ``role`` : Rôle de l'utilisateur (``client``, ``employe``, ``admin``)
            - ``email`` : Adresse email de l'utilisateur authentifié

    :ivar serializer_class: Sérialiseur personnalisé pour enrichir la réponse JWT
    :type serializer_class: CustomTokenObtainPairSerializer
    """

    serializer_class = CustomTokenObtainPairSerializer
