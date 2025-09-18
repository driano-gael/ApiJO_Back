"""
Module contenant le sérialiseur pour le modèle Discipline.

Ce module définit la sérialisation/désérialisation des données
des disciplines sportives pour l'API REST.
"""
from rest_framework import serializers
from api.models import Discipline


class DisciplineSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle Discipline.

    Permet la conversion entre les objets Discipline et leur représentation JSON
    pour les échanges via l'API REST. Inclut tous les champs du modèle.

    Fields:
        - nom: Nom de la discipline sportive
        - icone: Chemin ou nom de l'icône de la discipline
    """
    class Meta:
        model = Discipline
        fields = '__all__'