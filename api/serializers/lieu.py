from rest_framework import serializers
from api.models import Lieu

class LieuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lieu
        fields = '__all__'