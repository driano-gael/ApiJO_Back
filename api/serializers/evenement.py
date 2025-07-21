from rest_framework import serializers
from api.models import Evenement, Lieu
from api.serializers.lieu import LieuSerializer
from api.serializers.nested_serializer import NestedEpreuveSerializer


class EvenementSerializer(serializers.ModelSerializer):
    lieu = LieuSerializer(read_only=True)
    lieu_id = serializers.PrimaryKeyRelatedField(
        queryset=Lieu.objects.all(),
        write_only=True,
        source='lieu'
    )
    epreuves = NestedEpreuveSerializer(many=True, read_only=True)
    class Meta:
        model = Evenement
        fields = ['id', 'description', 'lieu', 'lieu_id','date','horraire', 'epreuves']