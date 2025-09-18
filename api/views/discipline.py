"""
Module de vues pour la gestion des disciplines sportives.

Ce module contient toutes les vues nécessaires pour effectuer des opérations CRUD
sur les disciplines, ainsi que des fonctionnalités de recherche par nom.
"""
import rest_framework.generics
from django.db.models import Q
from api.models.discipline import Discipline
from api.serializers.discipline import DisciplineSerializer
from authentication.permissions import *
from rest_framework.permissions import IsAuthenticated, AllowAny


class DisciplineListView(rest_framework.generics.ListAPIView):
    """
    Vue pour lister les disciplines avec possibilité de recherche.

    Permet de récupérer la liste des disciplines sportives disponibles.
    Supporte la recherche par nom via le paramètre 'search'.
    Les résultats sont triés par ordre alphabétique du nom.
    Accessible à tous les utilisateurs (authentifiés ou non).
    """
    serializer_class = DisciplineSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        """
        Récupère le queryset des disciplines avec filtrage optionnel.

        Returns:
            QuerySet: Les disciplines filtrées et triées par nom
        """
        queryset = Discipline.objects.all()
        search = self.request.GET.get('search', None)
        if search is not None:
            queryset = queryset.filter(
                Q(nom__istartswith=search)
            )
        return queryset.order_by('nom')

class DisciplineDetailView(rest_framework.generics.RetrieveAPIView):
    """
    Vue pour récupérer les détails d'une discipline spécifique.

    Permet de récupérer les informations détaillées d'une discipline
    via son identifiant unique.
    Accessible à tous les utilisateurs (authentifiés ou non).
    """
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = [AllowAny]

class DisciplineCreateView(rest_framework.generics.CreateAPIView):
    """
    Vue pour créer une nouvelle discipline.

    Permet aux administrateurs authentifiés de créer de nouvelles disciplines sportives.
    Nécessite une authentification et des permissions d'administrateur.
    """
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class DisciplineUpdateView(rest_framework.generics.UpdateAPIView):
    """
    Vue pour mettre à jour une discipline existante.

    Permet aux administrateurs authentifiés de modifier les informations
    d'une discipline existante.
    Nécessite une authentification et des permissions d'administrateur.
    """
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class DisciplineDeleteView(rest_framework.generics.DestroyAPIView):
    """
    Vue pour supprimer une discipline.

    Permet aux administrateurs authentifiés de supprimer une discipline existante.
    Nécessite une authentification et des permissions d'administrateur.
    """
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = [IsAuthenticated, IsAdmin]