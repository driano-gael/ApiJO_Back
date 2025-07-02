from rest_framework import serializers
from api.models import Epreuve
from api.serializers import LieuSerializer


class EpreuveSerializer(serializers.ModelSerializer):
    lieu = LieuSerializer()
    class Meta:
        model = Epreuve
        fields = '__all__'