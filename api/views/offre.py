"""
Module de vues pour la gestion des offres commerciales.

Ce module contient toutes les vues nécessaires pour effectuer des opérations CRUD
sur les offres, avec un tri par nombre de personnes et montant.
"""

import rest_framework.generics
from api.models import Offre
from api.serializers import OffreSerializer
from authentication.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated, AllowAny


class OffreListView(rest_framework.generics.ListAPIView):
    """
    Vue pour lister toutes les offres avec tri optimisé.

    Récupère la liste des offres triées par nombre de personnes puis par montant.
    Accessible à tous les utilisateurs (authentifiés ou non).

    :cvar queryset: Queryset des offres
    :type queryset: QuerySet[Offre]
    :cvar serializer_class: Sérialiseur utilisé pour la vue
    :type serializer_class: OffreSerializer
    :cvar permission_classes: Permissions requises pour accéder à la vue
    :type permission_classes: list
    """
    queryset = Offre.objects.order_by("nb_personne", "montant")
    serializer_class = OffreSerializer
    permission_classes = [IsAuthenticated]


class OffreDetailView(rest_framework.generics.RetrieveAPIView):
    """
    Vue pour récupérer les détails d'une offre spécifique.

    Permet de récupérer les informations détaillées d'une offre
    via son identifiant unique.
    Accessible à tous les utilisateurs (authentifiés ou non).

    :cvar queryset: Queryset des offres
    :type queryset: QuerySet[Offre]
    :cvar serializer_class: Sérialiseur utilisé pour la vue
    :type serializer_class: OffreSerializer
    :cvar permission_classes: Permissions requises pour accéder à la vue
    :type permission_classes: list
    """
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer
    permission_classes = [IsAuthenticated]


class OffreCreateView(rest_framework.generics.CreateAPIView):
    """
    Vue pour créer une nouvelle offre.

    Permet aux administrateurs authentifiés de créer de nouvelles offres commerciales.
    Nécessite une authentification et des permissions d'administrateur.

    :cvar queryset: Queryset des offres
    :type queryset: QuerySet[Offre]
    :cvar serializer_class: Sérialiseur utilisé pour la vue
    :type serializer_class: OffreSerializer
    :cvar permission_classes: Permissions requises pour accéder à la vue
    :type permission_classes: list
    """
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class OffreUpdateView(rest_framework.generics.UpdateAPIView):
    """
    Vue pour mettre à jour une offre existante.

    Permet aux administrateurs authentifiés de modifier les informations
    d'une offre existante.
    Nécessite une authentification et des permissions d'administrateur.

    :cvar queryset: Queryset des offres
    :type queryset: QuerySet[Offre]
    :cvar serializer_class: Sérialiseur utilisé pour la vue
    :type serializer_class: OffreSerializer
    :cvar permission_classes: Permissions requises pour accéder à la vue
    :type permission_classes: list
    """
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class OffreDeleteView(rest_framework.generics.DestroyAPIView):
    """
    Vue pour supprimer une offre.

    Permet aux administrateurs authentifiés de supprimer une offre existante.
    Nécessite une authentification et des permissions d'administrateur.

    :cvar queryset: Queryset des offres
    :type queryset: QuerySet[Offre]
    :cvar serializer_class: Sérialiseur utilisé pour la vue
    :type serializer_class: OffreSerializer
    :cvar permission_classes: Permissions requises pour accéder à la vue
    :type permission_classes: list
    """
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
