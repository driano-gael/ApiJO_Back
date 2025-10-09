"""
Sérialiseur pour le profil client.

Ce module définit la sérialisation/désérialisation des objets ClientProfile
pour l'API REST.
"""

from rest_framework import serializers
from users.models.client import ClientProfile
from users.serializers import UserSerializer


class ClientSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle ClientProfile.

    :ivar id: Identifiant unique du profil client (lecture seule)
    :vartype id: int
    :ivar user: Utilisateur associé au profil client (lecture seule)
    :vartype user: User
    :ivar nom: Nom de famille du client
    :vartype nom: str
    :ivar prenom: Prénom du client
    :vartype prenom: str
    :ivar telephone: Numéro de téléphone du client
    :vartype telephone: str
    """
    class Meta:
        model = ClientProfile
        fields = ['id', 'user', 'nom', 'prenom', 'telephone']
        read_only_fields = ['id', 'user']

    def create(self, validated_data):
        """
        Crée un nouveau profil client.

        :param validated_data: Données validées du serializer
        :type validated_data: dict
        :return: Instance ClientProfile créée
        :rtype: ClientProfile
        """
        return super().create(validated_data)


class ClientFullSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle ClientProfile.

    :ivar id: Identifiant unique du profil client (lecture seule)
    :vartype id: int
    :ivar user: Utilisateur associé au profil client (lecture seule)
    :vartype user: User
    :ivar nom: Nom de famille du client
    :vartype nom: str
    :ivar prenom: Prénom du client
    :vartype prenom: str
    :ivar telephone: Numéro de téléphone du client
    :vartype telephone: str
    """
    user = UserSerializer(read_only=True)
    class Meta:
        model = ClientProfile
        fields = ['id', 'user', 'nom', 'prenom', 'telephone', 'cle_chiffree']
        read_only_fields = ['id', 'user', 'cle_chiffree']