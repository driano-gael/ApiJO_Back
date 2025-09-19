"""
Module contenant le sérialiseur pour le modèle Lieu.

Ce module définit la sérialisation/désérialisation des données
des lieux sportifs pour l'API REST.
"""

from rest_framework import serializers
from api.models import Lieu

class LieuSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle Lieu.

    Permet la conversion entre les objets Lieu et leur représentation JSON
    pour les échanges via l'API REST. Inclut tous les champs du modèle.

    :ivar nom: Nom du lieu sportif
    :type nom: str
    """
    class Meta:
        """
        Configuration du sérialiseur.

        :cvar model: Modèle Django associé au sérialiseur
        :type model: Lieu
        :cvar fields: Champs inclus dans la sérialisation
        :type fields: str
        """
        model = Lieu
        fields = '__all__'
