"""
Sérialiseur pour le profil employé.

Ce module définit la sérialisation/désérialisation des objets EmployeProfile
pour l'API REST.
"""

from rest_framework import serializers
from users.models.employe import EmployeProfile
from users.serializers import UserSerializer


class EmployeSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle EmployeProfile.

    :ivar id: Identifiant unique du profil employé (lecture seule)
    :vartype id: int
    :ivar user: Utilisateur associé au profil employé (lecture seule)
    :vartype user: User
    :ivar nom: Nom de famille de l'employé
    :vartype nom: str
    :ivar prenom: Prénom de l'employé
    :vartype prenom: str
    :ivar matricule: Numéro de matricule unique de l'employé
    :vartype matricule: str
    :ivar identifiant_telephone: Identifiant téléphonique professionnel
    :vartype identifiant_telephone: str
    """
    user = UserSerializer(read_only=True)
    class Meta:
        model = EmployeProfile
        fields = ['id', 'user', 'nom', 'prenom', 'matricule', 'identifiant_telephone']
        read_only_fields = ['id', 'user']

    def create(self, validated_data):
        """
        Crée un nouveau profil employé.

        :param validated_data: Données validées du serializer
        :type validated_data: dict
        :return: Instance EmployeProfile créée
        :rtype: EmployeProfile
        """
        return super().create(validated_data)
