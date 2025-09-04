from rest_framework import serializers

from api.models import Lieu
from api.models.epreuve import Epreuve
from api.models.evenement import Evenement
from api.serializers import LieuSerializer


class NestedEpreuveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Epreuve
        fields = ['id', 'libelle', 'discipline']

class NestedEvenementSerializer(serializers.ModelSerializer):
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