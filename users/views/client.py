import rest_framework.generics
from authentication.permissions import IsAdmin
from users.models import ClientProfile
from users.serializers.client import ClientFullSerializer


class ClientListView(rest_framework.generics.ListAPIView):
    """
    Liste tous les clients.

    Cette vue renvoie tous les clients,
    triés par date de création (du plus ancien au plus récent).
    L'accès est restreint aux Administrateurs.

    :cvar serializer_class: Sérialiseur utilisé pour convertir les clients en JSON.
    :type serializer_class: ClientSerializer
    :cvar permission_classes: Permissions requises pour accéder à la vue.
    :type permission_classes: list[rest_framework.permissions.BasePermission]
    """

    serializer_class = ClientFullSerializer
    permission_classes = [IsAdmin]

    def get_queryset(self):
        """
        Retourne les clients.

        :return: Liste des clients.
        :rtype: QuerySet[Client]
        """
        return ClientProfile.objects.all().order_by("nom")