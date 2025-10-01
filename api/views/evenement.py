"""
Module de vues pour la gestion des événements.

Ce module contient toutes les vues nécessaires pour effectuer des opérations CRUD
sur les événements, ainsi que des vues spécialisées pour récupérer des événements
par épreuve.
"""

from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound

from api.models.evenement import Evenement
from api.models.epreuve import Epreuve
from api.serializers.evenement import EvenementSerializer
from authentication.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated, AllowAny


class EvenementListView(generics.ListAPIView):
    """
    Vue pour lister tous les événements.

    Récupère la liste complète des événements disponibles.
    Accessible à tous les utilisateurs (authentifiés ou non).

    :cvar queryset: Queryset des événements
    :type queryset: QuerySet[Evenement]
    :cvar serializer_class: Sérialiseur utilisé pour la vue
    :type serializer_class: EvenementSerializer
    :cvar permission_classes: Permissions requises pour accéder à la vue
    :type permission_classes: list
    """
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    permission_classes = [AllowAny]


class EvenementDetailView(generics.RetrieveAPIView):
    """
    Vue pour récupérer les détails d'un événement spécifique.

    Permet de récupérer les informations détaillées d'un événement
    via son identifiant unique.
    Accessible à tous les utilisateurs (authentifiés ou non).

    :cvar queryset: Queryset des événements
    :type queryset: QuerySet[Evenement]
    :cvar serializer_class: Sérialiseur utilisé pour la vue
    :type serializer_class: EvenementSerializer
    :cvar permission_classes: Permissions requises pour accéder à la vue
    :type permission_classes: list
    """
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    permission_classes = [AllowAny]



class EvenementByEpreuveView(generics.RetrieveAPIView):
    """
    Vue pour récupérer un événement par l'ID d'une épreuve.
    """
    serializer_class = EvenementSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        epreuve = get_object_or_404(Epreuve, id=self.kwargs["pk"])
        if epreuve.evenement is None:
            raise NotFound("Aucun événement associé à cette épreuve.")
        return epreuve.evenement


class EvenementCreateView(generics.CreateAPIView):
    """
    Vue pour créer un nouvel événement.

    Permet aux administrateurs authentifiés de créer de nouveaux événements.
    Nécessite une authentification et des permissions d'administrateur.

    :cvar queryset: Queryset des événements
    :type queryset: QuerySet[Evenement]
    :cvar serializer_class: Sérialiseur utilisé pour la vue
    :type serializer_class: EvenementSerializer
    :cvar permission_classes: Permissions requises pour accéder à la vue
    :type permission_classes: list
    """
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class EvenementUpdateView(generics.UpdateAPIView):
    """
    Vue pour mettre à jour un événement existant.

    Permet aux administrateurs authentifiés de modifier les informations
    d'un événement existant.
    Nécessite une authentification et des permissions d'administrateur.

    :cvar queryset: Queryset des événements
    :type queryset: QuerySet[Evenement]
    :cvar serializer_class: Sérialiseur utilisé pour la vue
    :type serializer_class: EvenementSerializer
    :cvar permission_classes: Permissions requises pour accéder à la vue
    :type permission_classes: list
    """
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class EvenementDeleteView(generics.DestroyAPIView):
    """
    Vue pour supprimer un événement.

    Permet aux administrateurs authentifiés de supprimer un événement existant.
    Nécessite une authentification et des permissions d'administrateur.

    :cvar queryset: Queryset des événements
    :type queryset: QuerySet[Evenement]
    :cvar serializer_class: Sérialiseur utilisé pour la vue
    :type serializer_class: EvenementSerializer
    :cvar permission_classes: Permissions requises pour accéder à la vue
    :type permission_classes: list
    """
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
