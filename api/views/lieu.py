"""
Module de vues pour la gestion des lieux sportifs.

Ce module contient toutes les vues nécessaires pour effectuer des opérations CRUD
sur les lieux où se déroulent les événements sportifs.
"""
import rest_framework.generics
from api.models import Lieu
from api.serializers import LieuSerializer
from authentication.permissions import *
from rest_framework.permissions import IsAuthenticated, AllowAny


class LieuListView(rest_framework.generics.ListAPIView):
    """
    Vue pour lister tous les lieux sportifs.

    Permet de récupérer la liste complète des lieux disponibles
    pour les événements sportifs.
    Accessible à tous les utilisateurs (authentifiés ou non).
    """
    queryset = Lieu.objects.all()
    serializer_class = LieuSerializer
    permission_classes = [AllowAny]

class LieuDetailView(rest_framework.generics.RetrieveAPIView):
    """
    Vue pour récupérer les détails d'un lieu spécifique.

    Permet de récupérer les informations détaillées d'un lieu
    via son identifiant unique.
    Accessible à tous les utilisateurs (authentifiés ou non).
    """
    queryset = Lieu.objects.all()
    serializer_class = LieuSerializer
    permission_classes = [AllowAny]

class LieuCreateView(rest_framework.generics.CreateAPIView):
    """
    Vue pour créer un nouveau lieu.

    Permet aux administrateurs authentifiés de créer de nouveaux lieux sportifs.
    Nécessite une authentification et des permissions d'administrateur.
    """
    queryset = Lieu.objects.all()
    serializer_class = LieuSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class LieuUpdateView(rest_framework.generics.UpdateAPIView):
    """
    Vue pour mettre à jour un lieu existant.

    Permet aux administrateurs authentifiés de modifier les informations
    d'un lieu existant.
    Nécessite une authentification et des permissions d'administrateur.
    """
    queryset = Lieu.objects.all()
    serializer_class = LieuSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class LieuDeleteView(rest_framework.generics.DestroyAPIView):
    """
    Vue pour supprimer un lieu.

    Permet aux administrateurs authentifiés de supprimer un lieu existant.
    Nécessite une authentification et des permissions d'administrateur.
    """
    queryset = Lieu.objects.all()
    serializer_class = LieuSerializer
    permission_classes = [IsAuthenticated, IsAdmin]