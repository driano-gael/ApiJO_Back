from rest_framework import serializers
from api.models import Epreuve, Discipline, Evenement
from api.serializers.discipline import DisciplineSerializer
from api.serializers.nested_serializer import NestedEvenementSerializer


class EpreuveSerializer(serializers.ModelSerializer):
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
        fields = ['id', 'libelle', 'discipline', 'evenement', 'discipline_id', 'evenement_id']