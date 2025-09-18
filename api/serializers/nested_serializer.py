"""
Module contenant les sérialiseurs imbriqués pour éviter les références circulaires.

Ce module définit des versions simplifiées des sérialiseurs pour être utilisées
dans les relations entre modèles sans créer d'imports circulaires.
"""
from rest_framework import serializers

from api.models import Lieu
from api.models.epreuve import Epreuve
from api.models.evenement import Evenement
from api.serializers import LieuSerializer


class NestedEpreuveSerializer(serializers.ModelSerializer):
    """
    Sérialiseur imbriqué pour le modèle Epreuve.

    Version simplifiée du sérialiseur d'épreuve utilisée dans les relations
    pour éviter les imports circulaires. N'inclut que les champs essentiels.

    Fields:
        - id: Identifiant unique de l'épreuve
        - libelle: Intitulé de l'épreuve
        - discipline: Discipline associée
    """
    class Meta:
        model = Epreuve
        fields = ['id', 'libelle', 'discipline']

class NestedEvenementSerializer(serializers.ModelSerializer):
    """
    Sérialiseur imbriqué pour le modèle Evenement.

    Version simplifiée du sérialiseur d'événement utilisée dans les relations
    pour éviter les imports circulaires. Inclut les informations de base
    avec la gestion du lieu.

    Fields:
        - id: Identifiant unique de l'événement
        - description: Description de l'événement
        - date: Date de l'événement
        - horraire: Heure de l'événement
        - lieu: Données du lieu (lecture seule)
        - lieu_id: ID du lieu pour l'écriture
    """
    lieu = LieuSerializer(read_only=True)
    lieu_id = serializers.PrimaryKeyRelatedField(
        queryset=Lieu.objects.all(),
        write_only=True,
        source='lieu'
    )
    class Meta:
        model = Evenement
        fields = ['id',
                  'description',
                  'date',
                  'lieu_id',
                  'lieu',
                  'date',
                  'horraire']