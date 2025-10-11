"""
Vues pour l'inscription des clients.

Ce module contient les vues nécessaires pour gérer l'inscription
des nouveaux clients via l'API REST.

:module: authentication.views.client
"""

from rest_framework import generics
from rest_framework.permissions import AllowAny

from authentication.permissions import IsAdmin
from authentication.serializers.client import ClientRegisterSerializer
from users.models.base_user import User

class ClientRegisterView(generics.CreateAPIView):
    """
    Vue pour l'inscription des clients.

    Permet à un utilisateur de créer un compte client avec validation
    des données personnelles et création automatique du profil.

    Accessible à tous (pas d'authentification requise).

    :methods:
        - POST: Créer un nouveau compte client
    :ivar queryset: Queryset de base pour les clients
    :type queryset: QuerySet[User]
    :ivar serializer_class: Sérialiseur utilisé pour la création
    :type serializer_class: ClientRegisterSerializer
    :ivar permission_classes: Permissions appliquées à la vue
    :type permission_classes: list
    """
    queryset = User.objects.all()
    serializer_class = ClientRegisterSerializer
    permission_classes = [AllowAny]