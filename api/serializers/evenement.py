"""
Module contenant le sérialiseur pour le modèle Evenement.

Ce module définit la sérialisation/désérialisation des données des événements
sportifs pour l'API REST, incluant la gestion des relations avec les épreuves et lieux.
"""
from rest_framework import serializers
from api.models import Evenement, Lieu, Epreuve
from api.serializers.lieu import LieuSerializer
from api.serializers.epreuve import EpreuveSerializer


class EvenementSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle Evenement.

    Gère la sérialisation des événements avec leurs relations aux épreuves et lieux.
    Permet l'assignation d'épreuves à un événement tout en évitant les conflits.

    :ivar epreuves: Liste des épreuves associées (lecture seule)
    :type epreuves: list of EpreuveSerializer
    :ivar epreuve_ids: IDs des épreuves à associer (écriture seule)
    :type epreuve_ids: PrimaryKeyRelatedField
    :ivar lieu: Données complètes du lieu (lecture seule)
    :type lieu: LieuSerializer
    :ivar lieu_id: ID du lieu pour l'écriture
    :type lieu_id: PrimaryKeyRelatedField
    """
    epreuves = EpreuveSerializer(many=True, read_only=True)
    epreuve_ids = serializers.PrimaryKeyRelatedField(
        queryset=Epreuve.objects.all(),
        many=True,
        write_only=True,
        source='epreuves',
        required=False
    )
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
        fields = [
            'id', 'description',
            'lieu', 'lieu_id',
            'date', 'horraire',
            'epreuves', 'epreuve_ids',
            'nb_place_total', 'nb_place_restante'
        ]

    def validate_epreuve_ids(self, value):
        """
        Valide les IDs des épreuves à associer à l'événement.

        Vérifie qu'aucune épreuve n'est déjà assignée à un autre événement
        pour éviter les conflits d'assignation.

        :param value: Liste des épreuves à valider
        :type value: list of Epreuve
        :return: Liste des épreuves validées
        :rtype: list of Epreuve
        :raises serializers.ValidationError: Si des épreuves sont déjà assignées ailleurs
        """
        if not value:
            return value

        # Vérifier les conflits en excluant l'événement actuel (si modification)
        instance_id = self.instance.id if self.instance else None
        conflits = []

        for epreuve in value:
            if epreuve.evenement_id is not None and epreuve.evenement_id != instance_id:
                conflits.append(epreuve)

        if conflits:
            raise serializers.ValidationError(
                f"Les épreuves suivantes sont déjà assignées à d'autres événements : {[e.id for e in conflits]}"
            )
        return value

    def create(self, validated_data):
        """
        Crée un nouvel événement avec ses épreuves associées.

        :param validated_data: Données validées pour la création
        :type validated_data: dict
        :return: L'événement créé avec ses épreuves assignées
        :rtype: Evenement
        """
        epreuves = validated_data.pop('epreuves', [])
        evenement = Evenement.objects.create(**validated_data)

        for epreuve in epreuves:
            epreuve.evenement = evenement
            epreuve.save()

        return evenement

    def update(self, instance, validated_data):
        """
        Met à jour un événement et gère les épreuves associées.

        Désassocie les anciennes épreuves et assigne les nouvelles si présentes.

        :return: L'événement mis à jour
        """
        epreuves = validated_data.pop('epreuves', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if epreuves is not None:
            nouveaux_ids = {e.pk for e in epreuves}
            anciens_ids = set(instance.epreuves.values_list('id', flat=True))

            # Désassocier les épreuves qui ne sont plus dans la liste
            instance.epreuves.filter(id__in=anciens_ids - nouveaux_ids).update(evenement=None)

            # Associer les nouvelles épreuves
            for epreuve in epreuves:
                if epreuve.pk not in anciens_ids:
                    epreuve.evenement = instance
                    epreuve.save()

        return instance
