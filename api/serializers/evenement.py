from rest_framework import serializers
from api.models import Evenement, Lieu, Epreuve
from api.serializers.lieu import LieuSerializer
from api.serializers.epreuve import EpreuveSerializer


class EvenementSerializer(serializers.ModelSerializer):
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

    def validate_epreuve_ids(self, value):
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
        epreuves = validated_data.pop('epreuves', [])
        evenement = Evenement.objects.create(**validated_data)

        for epreuve in epreuves:
            epreuve.evenement = evenement
            epreuve.save()

        return evenement

    def update(self, instance, validated_data):
        epreuves = validated_data.pop('epreuves', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if epreuves is not None:
            nouveaux_ids = {e.pk for e in epreuves}
            anciens_ids = set(instance.epreuves.values_list('id', flat=True))

            instance.epreuves.filter(id__in=anciens_ids - nouveaux_ids).update(evenement=None)

            for epreuve in epreuves:
                if epreuve.pk not in anciens_ids:
                    epreuve.evenement = instance
                    epreuve.save()

        return instance

    class Meta:
        model = Evenement
        fields = [
            'id', 'description',
            'lieu', 'lieu_id',
            'date', 'horraire',
            'epreuves', 'epreuve_ids'
        ]
