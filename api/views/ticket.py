from api.serializers import TicketSerializer, OffreSerializer, EvenementSerializer
from rest_framework.permissions import IsAuthenticated
from api.serializers.ticket import PanierItemSerializer
from rest_framework import generics


class TicketListView(generics.ListAPIView):
    """
    Liste les tickets appartenant à l'utilisateur connecté.

    Cette vue renvoie uniquement les tickets de l'utilisateur authentifié,
    triés par date d'achat (du plus ancien au plus récent).
    L'accès est restreint aux utilisateurs authentifiés.

    :cvar serializer_class: Sérialiseur utilisé pour convertir les tickets en JSON.
    :type serializer_class: TicketSerializer
    :cvar permission_classes: Permissions requises pour accéder à la vue.
    :type permission_classes: list[rest_framework.permissions.BasePermission]
    """

    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Retourne les tickets de l'utilisateur actuellement connecté.

        Cette méthode filtre le queryset des tickets pour ne conserver
        que ceux associés à `request.user` et les trie par `date_achat`.

        :return: Liste des tickets de l'utilisateur connecté.
        :rtype: QuerySet[Ticket]
        """
        return Ticket.objects.filter(client=self.request.user.client_profile).order_by("date_achat")

class TicketDetailView(generics.RetrieveAPIView):
    """
    Récupère les détails d'un ticket spécifique appartenant à l'utilisateur connecté.

    Cette vue permet à un utilisateur authentifié de voir les détails
    d'un ticket qu'il possède, identifié par son ID.
    L'accès est restreint aux utilisateurs authentifiés.

    :cvar serializer_class: Sérialiseur utilisé pour convertir le ticket en JSON.
    :type serializer_class: TicketSerializer
    :cvar permission_classes: Permissions requises pour accéder à la vue.
    :type permission_classes: list[rest_framework.permissions.BasePermission]
    """

    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Retourne les tickets de l'utilisateur actuellement connecté.

        Cette méthode filtre le queryset des tickets pour ne conserver
        que ceux associés à `request.user`.

        :return: Liste des tickets de l'utilisateur connecté.
        :rtype: QuerySet[Ticket]
        """
        return Ticket.objects.filter(client=self.request.user.client_profile)




from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from api.models import Ticket


class TicketBatchCreateView(generics.GenericAPIView):
    """
    Vue pour créer plusieurs tickets à partir du panier de l'utilisateur connecté.

    Reçoit un tableau `items` contenant `offreId`, `evenementId` et `quantity`.
    Crée autant de tickets que possible pour chaque offre.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PanierItemSerializer

    def post(self, request, *args, **kwargs):
        items_data = request.data.get("items")
        if not items_data or not isinstance(items_data, list):
            return Response(
                {"detail": "Le champ 'items' est requis et doit être un tableau."},
                status=status.HTTP_400_BAD_REQUEST
            )

        client_profile = getattr(request.user, 'client_profile', None)
        if not client_profile:
            return Response(
                {'detail': "Client introuvable."},
                status=status.HTTP_400_BAD_REQUEST
            )

        tickets_created = []
        tickets_uncreated = []

        for item_data in items_data:
            serializer = self.get_serializer(data=item_data)
            serializer.is_valid(raise_exception=True)

            offre = serializer.validated_data['offre']
            evenement = serializer.validated_data['evenement']
            quantity = serializer.validated_data['quantity']

            for _ in range(quantity):
                if evenement.nb_place_restante >= offre.nb_personne:
                    evenement.nb_place_restante -= offre.nb_personne
                    evenement.save()
                    ticket = Ticket(
                        client=client_profile,
                        evenement=evenement,
                        offre=offre,
                        statut='valide'
                    )
                    ticket.save()
                    tickets_created.append(ticket)

                else:
                    tickets_uncreated.append({
                        "offre": offre.libelle,
                        "evenement": evenement.description,
                        "reason": "Places insuffisantes"
                    })

        serrialised_ticket = TicketSerializer(tickets_created, many=True)
        return Response(
            {"tickets": serrialised_ticket.data, "erreurs": tickets_uncreated},
            status=status.HTTP_201_CREATED
        )
