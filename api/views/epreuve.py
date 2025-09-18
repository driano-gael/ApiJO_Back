"""
Module de vues pour la gestion des épreuves sportives.

Ce module contient toutes les vues nécessaires pour effectuer des opérations CRUD
sur les épreuves, avec un tri optimisé par discipline, date et horaire.
"""

import rest_framework.generics
from api.models.epreuve import Epreuve
from api.serializers.epreuve import EpreuveSerializer
from authentication.permissions import *
from rest_framework.permissions import IsAuthenticated, AllowAny


class EpreuveListView(rest_framework.generics.ListAPIView):
    """
    Vue pour lister toutes les épreuves avec tri optimisé.

    Récupère la liste des épreuves triées par discipline, date et horaire.
    Utilise select_related pour optimiser les requêtes vers la base de données.
    Accessible à tous les utilisateurs (authentifiés ou non).
    """
    queryset = Epreuve.objects.select_related("evenement", "discipline").order_by(
        "discipline__nom","evenement__date", "evenement__horraire"
    )
    serializer_class = EpreuveSerializer
    permission_classes = [AllowAny]

class EpreuveDetailView(rest_framework.generics.RetrieveAPIView):
    """
    Vue pour récupérer les détails d'une épreuve spécifique.

    Permet de récupérer les informations détaillées d'une épreuve
    via son identifiant unique.
    Accessible à tous les utilisateurs (authentifiés ou non).
    """
    queryset = Epreuve.objects.all()
    serializer_class = EpreuveSerializer
    permission_classes = [AllowAny]

class EpreuveCreateView(rest_framework.generics.CreateAPIView):
    """
    Vue pour créer une nouvelle épreuve.

    Permet aux administrateurs authentifiés de créer de nouvelles épreuves sportives.
    Nécessite une authentification et des permissions d'administrateur.
    """
    queryset = Epreuve.objects.all()
    serializer_class = EpreuveSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class EpreuveUpdateView(rest_framework.generics.UpdateAPIView):
    """
    Vue pour mettre à jour une épreuve existante.

    Permet aux administrateurs authentifiés de modifier les informations
    d'une épreuve existante.
    Nécessite une authentification et des permissions d'administrateur.
    """
    queryset = Epreuve.objects.all()
    serializer_class = EpreuveSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class EpreuveDeleteView(rest_framework.generics.DestroyAPIView):
    """
    Vue pour supprimer une épreuve.

    Permet aux administrateurs authentifiés de supprimer une épreuve existante.
    Nécessite une authentification et des permissions d'administrateur.
    """
    queryset = Epreuve.objects.all()
    serializer_class = EpreuveSerializer
    permission_classes = [IsAuthenticated, IsAdmin]