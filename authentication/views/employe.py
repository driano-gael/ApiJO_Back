"""
Vues pour l'inscription des employés.

Ce module contient les vues nécessaires pour gérer l'inscription
des nouveaux employés via l'API REST (accès admin uniquement).

:module: authentication.views.employee
"""

from rest_framework import generics
from authentication.permissions import IsAdmin
from authentication.serializers.employee import EmployeeRegisterSerializer
from users.models.employe import EmployeProfile


class EmployeeRegisterView(generics.CreateAPIView):
    """
    Vue pour l'inscription des employés.

    Permet aux administrateurs de créer des comptes employé avec validation
    des données professionnelles et création automatique du profil.

    Nécessite des privilèges d'administrateur.

    :methods:
        - POST: Créer un nouveau compte employé (admin uniquement)

    :ivar queryset: Queryset de base pour les profils employés
    :type queryset: QuerySet[EmployeProfile]
    :ivar serializer_class: Sérialiseur utilisé pour la création
    :type serializer_class: EmployeeRegisterSerializer
    :ivar permission_classes: Permissions appliquées à la vue
    :type permission_classes: list
    """
    queryset = EmployeProfile.objects.all()
    serializer_class = EmployeeRegisterSerializer
    permission_classes = [IsAdmin]
