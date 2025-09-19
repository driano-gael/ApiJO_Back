"""
Sérialiseur pour le profil administrateur.

Ce module définit la sérialisation/désérialisation des données
du profil Admin pour l'API REST. Permet de convertir entre
l'objet AdminProfile et sa représentation JSON.
"""

from rest_framework import serializers
from users.models.admin import AdminProfile


class AdminSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle AdminProfile.

    :ivar id: Identifiant unique du profil admin (lecture seule)
    :vartype id: int
    :ivar user: Référence à l'utilisateur associé (lecture seule)
    :vartype user: User
    :ivar nom: Nom de famille de l'administrateur
    :vartype nom: str
    :ivar prenom: Prénom de l'administrateur
    :vartype prenom: str
    :ivar matricule: Identifiant unique de l'administrateur
    :vartype matricule: str
    """

    class Meta:
        model = AdminProfile
        fields = ['id', 'user', 'nom', 'prenom', 'matricule']
        read_only_fields = ['id', 'user']
