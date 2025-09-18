"""
Vues pour l'inscription des employés.

Ce module contient les vues nécessaires pour gérer l'inscription
des nouveaux employés via l'API REST (accès admin uniquement).
"""

from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from authentication.serializers.employee import EmployeeRegisterSerializer
from users.models.employe import EmployeProfile

class EmployeeRegisterView(generics.CreateAPIView):
    """
    Vue pour l'inscription des employés.

    Permet aux administrateurs de créer des comptes employé avec validation
    des données professionnelles et création automatique du profil.
    Nécessite des privilèges d'administrateur.

    Methods:
        POST: Créer un nouveau compte employé (admin uniquement)
    """
    queryset = EmployeProfile.objects.all()
    serializer_class = EmployeeRegisterSerializer
    permission_classes = [IsAdminUser]