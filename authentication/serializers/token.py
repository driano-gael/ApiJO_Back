"""
Sérialiseur personnalisé pour l'authentification JWT.

Ce module étend le sérialiseur JWT par défaut pour ajouter des informations
spécifiques au rôle de l'utilisateur dans la réponse d'authentification.
"""

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import serializers
from users.models.base_user import User as CustomUser

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Sérialiseur personnalisé pour l'obtention des tokens JWT.

    Étend le sérialiseur JWT standard pour inclure le rôle et l'email
    de l'utilisateur dans la réponse d'authentification.

    Returns dans data:
        - access: Token d'accès JWT
        - refresh: Token de rafraîchissement JWT
        - role: Rôle de l'utilisateur (client, employe, admin)
        - email: Email de l'utilisateur authentifié
    """

    def validate(self, attrs):
        """
        Valide les identifiants et enrichit la réponse avec les données utilisateur.

        Args:
            attrs (dict): Attributs contenant email et password

        Returns:
            dict: Données du token enrichies avec rôle et email

        Raises:
            ValidationError: Si les identifiants sont invalides ou manquants
        """
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise serializers.ValidationError("Identifiants invalides.")
            assert isinstance(user, CustomUser)
        else:
            raise serializers.ValidationError("Email et mot de passe requis.")

        data = super().validate(attrs)
        data['role'] = user.role
        data['email'] = user.email
        return data
