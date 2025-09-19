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

    Attributes:
        nom (str): Nom de la discipline sportive
        icone (str): Chemin ou nom de l'icône de la discipline
    """
    class Meta:
        """
        Configuration du sérialiseur.

        Attributes:
            model (Model): Modèle Django associé au sérialiseur
            fields (str): Champs inclus dans la sérialisation
        """
        model = Discipline
        fields = '__all__'
