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

    :ivar libelle: Nom de l'offre
    :type libelle: str
    :ivar nb_personne: Nombre de personnes concernées par l'offre
    :type nb_personne: int
    :ivar montant: Montant de l'offre en euros
    :type montant: float
    :ivar description: Description détaillée de l'offre
    :type description: str
    """
    class Meta:
        """
        Configuration du sérialiseur.

        :cvar model: Modèle Django associé au sérialiseur
        :type model: Offre
        :cvar fields: Champs inclus dans la sérialisation
        :type fields: str
        """
        model = Offre
        fields = '__all__'
