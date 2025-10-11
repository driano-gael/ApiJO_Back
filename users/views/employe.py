import rest_framework.generics
from authentication.permissions import IsAdmin
from users.models import EmployeProfile
from users.serializers import EmployeSerializer


class EmployeListView(rest_framework.generics.ListAPIView):
    """
    Liste tous les employés.

    Cette vue renvoie tous les employés,
    triés par date de création (du plus ancien au plus récent).
    L'accès est restreint aux Administrateurs.

    :cvar permission_classes: Permissions requises pour accéder à la vue.
    :type permission_classes: list[rest_framework.permissions.BasePermission]
    """

    serializer_class = EmployeSerializer
    permission_classes = [IsAdmin]

    def get_queryset(self):
        """
        Retourne les clients.

        :return: Liste des clients.
        :rtype: QuerySet[Client]
        """
        return EmployeProfile.objects.all().order_by("nom")

class EmployeSetInactiveView(rest_framework.generics.UpdateAPIView):
    """
    Met un employé en inactif.

    Cette vue permet aux administrateurs de désactiver un compte employé.
    L'accès est restreint aux Administrateurs.

    :cvar serializer_class: Sérialiseur utilisé pour la mise à jour.
    :cvar permission_classes: Permissions requises pour accéder à la vue.
    :type permission_classes: list[rest_framework.permissions.BasePermission]
    """

    queryset = EmployeProfile.objects.all()
    serializer_class = EmployeSerializer
    permission_classes = [IsAdmin]

    def perform_update(self, serializer):
        """
        Met à jour le statut actif du client.

        :param serializer: Sérialiseur avec les données mises à jour.
        :type serializer: ClientFullSerializer
        """
        employe = serializer.instance
        user = employe.user
        user.is_active = not user.is_active
        user.save()
        serializer.save()