"""
Module contenant le sérialiseur pour le modèle Epreuve.

Ce module définit la sérialisation/désérialisation des données des épreuves
sportives pour l'API REST, incluant la validation des doublons.
"""

from rest_framework import serializers
from api.models import Epreuve, Discipline, Evenement
from api.serializers.discipline import DisciplineSerializer
from api.serializers.nested_serializer import NestedEvenementSerializer


class EpreuveSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle Epreuve.

    Gère la sérialisation des épreuves avec leurs relations aux disciplines et événements.
    Inclut une validation pour éviter les doublons d'épreuves dans une même discipline.

    Fields:
        - id: Identifiant unique de l'épreuve
        - libelle: Intitulé de l'épreuve
        - discipline: Données complètes de la discipline (lecture seule)
        - discipline_id: ID de la discipline pour l'écriture
        - evenement: Données de l'événement associé (lecture seule)
        - evenement_id: ID de l'événement pour l'écriture (optionnel)
        - genre: Genre de l'épreuve (homme, femme, mixte)
        - tour: Tour de l'épreuve (finale, demi-finale, etc.)
    """
    discipline = DisciplineSerializer(read_only=True)
    discipline_id = serializers.PrimaryKeyRelatedField(
        queryset=Discipline.objects.all(),
        write_only=True,
        source='discipline',
    )
    evenement = NestedEvenementSerializer(read_only=True)
    evenement_id = serializers.PrimaryKeyRelatedField(
        queryset=Evenement.objects.all(),
        write_only=True,
        source='evenement',
        required=False,
        allow_null=True,
    )

    def validate(self, data):
        """
        Valide les données de l'épreuve pour éviter les doublons.

        Vérifie qu'aucune épreuve avec le même libellé n'existe déjà
        pour la même discipline.

        Args:
            data: Données à valider

        Returns:
            dict: Données validées

        Raises:
            ValidationError: Si une épreuve similaire existe déjà
        """
        discipline = data.get('discipline') or self.instance.discipline
        libelle = data.get('libelle') or self.instance.libelle

        if Epreuve.objects.exclude(pk=self.instance.pk if self.instance else None).filter(
            libelle=libelle,
            discipline=discipline
        ).exists():
            raise serializers.ValidationError(
                "Une épreuve avec ce libellé existe déjà pour cette discipline."
            )
        return data

    class Meta:
        model = Epreuve
        fields = ['id',
                  'libelle',
                  'discipline',
                  'evenement',
                  'discipline_id',
                  'evenement_id',
                  'genre',
                  'tour']