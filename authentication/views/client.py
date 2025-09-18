"""
Vues pour l'inscription des clients.

Ce module contient les vues nécessaires pour gérer l'inscription
des nouveaux clients via l'API REST.
"""

from rest_framework import generics
from authentication.serializers.client import ClientRegisterSerializer
from rest_framework.permissions import AllowAny
from users.models.base_user import User

class ClientRegisterView(generics.CreateAPIView):
    """
    Vue pour l'inscription des clients.

    Permet à un utilisateur de créer un compte client avec validation
    des données personnelles et création automatique du profil.
    Accessible à tous (pas d'authentification requise).

    Methods:
        POST: Créer un nouveau compte client
    """
    queryset = User.objects.all()
    serializer_class = ClientRegisterSerializer
    permission_classes = [AllowAny]