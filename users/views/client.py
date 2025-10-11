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

class ClientSetInactiveView(rest_framework.generics.UpdateAPIView):
    """
    Met un client en inactif.

    Cette vue permet aux administrateurs de désactiver un compte client.
    L'accès est restreint aux Administrateurs.

    :cvar queryset: Queryset des clients.
    :type queryset: QuerySet[ClientProfile]
    :cvar serializer_class: Sérialiseur utilisé pour la mise à jour.
    :type serializer_class: ClientFullSerializer
    :cvar permission_classes: Permissions requises pour accéder à la vue.
    :type permission_classes: list[rest_framework.permissions.BasePermission]
    """

    queryset = ClientProfile.objects.all()
    serializer_class = ClientFullSerializer
    permission_classes = [IsAdmin]

    def perform_update(self, serializer):
        """
        Met à jour le statut actif du client.

        :param serializer: Sérialiseur avec les données mises à jour.
        :type serializer: ClientFullSerializer
        """
        client = serializer.instance
        user = client.user
        user.is_active = not user.is_active
        user.save()
        serializer.save()