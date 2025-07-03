from rest_framework import serializers
from api.models import Evenement, Lieu
from api.serializers import LieuSerializer


class EvenementSerializer(serializers.ModelSerializer):
    lieu = LieuSerializer(read_only=True)
    lieu_id = serializers.PrimaryKeyRelatedField(
        queryset=Lieu.objects.all(),
        write_only=True,
        source='lieu',
    )
    class Meta:
        model = Evenement
        fields = ['id', 'description', 'lieu', 'lieu_id','date','horraire']