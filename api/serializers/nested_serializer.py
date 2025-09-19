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

    :ivar id: Identifiant unique de l'épreuve
    :type id: int
    :ivar libelle: Intitulé de l'épreuve
    :type libelle: str
    :ivar discipline: Discipline associée
    :type discipline: Discipline
    """
    class Meta:
        """
        Configuration du sérialiseur.

        :cvar model: Modèle Django associé au sérialiseur
        :type model: Epreuve
        :cvar fields: Champs inclus dans la sérialisation
        :type fields: list
        """
        model = Epreuve
        fields = ['id', 'libelle', 'discipline']


class NestedEvenementSerializer(serializers.ModelSerializer):
    """
    Sérialiseur imbriqué pour le modèle Evenement.

    Version simplifiée du sérialiseur d'événement utilisée dans les relations
    pour éviter les imports circulaires. Inclut les informations de base
    avec la gestion du lieu.

    :ivar id: Identifiant unique de l'événement
    :type id: int
    :ivar description: Description de l'événement
    :type description: str
    :ivar date: Date de l'événement
    :type date: date
    :ivar horraire: Heure de l'événement
    :type horraire: time
    :ivar lieu: Données du lieu (lecture seule)
    :type lieu: LieuSerializer
    :ivar lieu_id: ID du lieu pour l'écriture
    :type lieu_id: PrimaryKeyRelatedField
    """
    lieu = LieuSerializer(read_only=True)
    lieu_id = serializers.PrimaryKeyRelatedField(
        queryset=Lieu.objects.all(),
        write_only=True,
        source='lieu'
    )

    class Meta:
        """
        Configuration du sérialiseur.

        :cvar model: Modèle Django associé au sérialiseur
        :type model: Evenement
        :cvar fields: Champs inclus dans la sérialisation
        :type fields: list
        """
        model = Evenement
        fields = ['id', 'description', 'date', 'horraire', 'lieu', 'lieu_id']
