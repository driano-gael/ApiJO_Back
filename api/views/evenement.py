"""
Module de vues pour la gestion des événements.

Ce module contient toutes les vues nécessaires pour effectuer des opérations CRUD
sur les événements, ainsi que des vues spécialisées pour récupérer des événements
par épreuve.
"""
import rest_framework.generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.evenement import Evenement
from api.models.epreuve import Epreuve
from api.serializers.evenement import EvenementSerializer
from authentication.permissions import *
from rest_framework.permissions import IsAuthenticated, AllowAny


class EvenementListView(rest_framework.generics.ListAPIView):
    """
    Vue pour lister tous les événements.

    Permet de récupérer la liste complète des événements disponibles.
    Accessible à tous les utilisateurs (authentifiés ou non).
    """
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    permission_classes = [AllowAny]

class EvenementDetailView(rest_framework.generics.RetrieveAPIView):
    """
    Vue pour récupérer les détails d'un événement spécifique.

    Permet de récupérer les informations détaillées d'un événement
    via son identifiant unique.
    Accessible à tous les utilisateurs (authentifiés ou non).
    """
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    permission_classes = [AllowAny]

class EvenementByEpreuveView(APIView):
    """
    Vue pour récupérer un événement par l'ID d'une épreuve.

    Permet de récupérer l'événement associé à une épreuve spécifique.
    Retourne une erreur 404 si aucun événement n'est associé à l'épreuve.
    Accessible à tous les utilisateurs (authentifiés ou non).
    """
    permission_classes = [AllowAny]

    def get(self, request, pk, *args, **kwargs):
        """
        Récupère l'événement associé à une épreuve.

        Args:
            request: La requête HTTP
            pk (int): L'identifiant de l'épreuve

        Returns:
            Response: Les données de l'événement ou une erreur 404
        """
        epreuve = get_object_or_404(Epreuve, id=pk)
        evenement = epreuve.evenement
        if evenement is None:
            return Response({"detail": "Aucun événement associé à cette épreuve."}, status=404)
        serializer = EvenementSerializer(evenement)
        return Response(serializer.data)


class EvenementCreateView(rest_framework.generics.CreateAPIView):
    """
    Vue pour créer un nouvel événement.

    Permet aux administrateurs authentifiés de créer de nouveaux événements.
    Nécessite une authentification et des permissions d'administrateur.
    """
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class EvenementUpdateView(rest_framework.generics.UpdateAPIView):
    """
    Vue pour mettre à jour un événement existant.

    Permet aux administrateurs authentifiés de modifier les informations
    d'un événement existant.
    Nécessite une authentification et des permissions d'administrateur.
    """
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class EvenementDeleteView(rest_framework.generics.DestroyAPIView):
    """
    Vue pour supprimer un événement.

    Permet aux administrateurs authentifiés de supprimer un événement existant.
    Nécessite une authentification et des permissions d'administrateur.
    """
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    permission_classes = [IsAuthenticated, IsAdmin]