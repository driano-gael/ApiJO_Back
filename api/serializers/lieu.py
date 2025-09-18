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

    Fields:
        - nom: Nom du lieu sportif
    """
    class Meta:
        model = Lieu
        fields = '__all__'