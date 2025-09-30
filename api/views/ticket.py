import rest_framework.generics
from api.models import Ticket
from api.serializers import TicketSerializer
from rest_framework.permissions import IsAuthenticated
from api.models import Offre, Evenement

class TicketListView(rest_framework.generics.ListAPIView):
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
        return Ticket.objects.filter(user=self.request.user).order_by("date_achat")

class TicketDetailView(rest_framework.generics.RetrieveAPIView):
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
        return Ticket.objects.filter(user=self.request.user)

class TicketCreateView(rest_framework.generics.CreateAPIView):
    """
    Crée un nouveau ticket pour l'utilisateur connecté.

    Cette vue permet à un utilisateur authentifié de créer un nouveau ticket.
    Le ticket sera automatiquement associé au ClientProfile de l'utilisateur,
    à l'offre choisie et à l'événement lié à l'offre. Les champs qr_code et key
    sont générés automatiquement.
    L'accès est restreint aux utilisateurs authentifiés.

    :cvar serializer_class: Sérialiseur utilisé pour valider et créer le ticket.
    :type serializer_class: TicketSerializer
    :cvar permission_classes: Permissions requises pour accéder à la vue.
    :type permission_classes: list[rest_framework.permissions.BasePermission]
    """
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Crée un ticket pour l'utilisateur connecté à partir d'une offre.

        Le corps de la requête doit contenir l'identifiant de l'offre.
        Le ticket sera associé au client, à l'offre et à l'événement correspondant.
        Les champs qr_code et key sont générés automatiquement.

        :param request: Requête HTTP contenant l'identifiant de l'offre.
        :type request: rest_framework.request.Request
        :return: Réponse avec le ticket créé ou une erreur.
        :rtype: rest_framework.response.Response
        """
        offre_id = request.data.get('offreID')
        if not offre_id:
            return Response({'detail': "Le champ 'offre' est requis."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            offre = Offre.objects.get(pk=offre_id)
        except Offre.DoesNotExist:
            return Response({'detail': "Offre introuvable."}, status=status.HTTP_404_NOT_FOUND)
        client_profile = getattr(request.user, 'clientprofile', None)
        if not client_profile:
            return Response({'detail': "Profil client introuvable pour l'utilisateur."}, status=status.HTTP_400_BAD_REQUEST)
        evenement = request.data.get('evenementID')
        ticket = Ticket(
            client=client_profile,
            evenement=offre.evenement,
            offre=offre,
            qr_code=str(uuid.uuid4()),
            statut='valide'
        )
        ticket.save()
        serializer = self.get_serializer(ticket)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
