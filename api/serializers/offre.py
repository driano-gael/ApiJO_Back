"""
Module contenant le sérialiseur pour le modèle Offre.

Ce module définit la sérialisation/désérialisation des données
des offres commerciales pour l'API REST.
"""

from rest_framework import serializers
from api.models import Offre

class OffreSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle Offre.

    Permet la conversion entre les objets Offre et leur représentation JSON
    pour les échanges via l'API REST. Inclut tous les champs du modèle.

    Fields:
        - libelle: Nom de l'offre
        - nb_personne: Nombre de personnes concernées par l'offre
        - montant: Montant de l'offre en euros
        - description: Description détaillée de l'offre
    """
    class Meta:
        model = Offre
        fields = '__all__'