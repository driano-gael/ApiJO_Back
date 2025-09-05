from rest_framework import serializers
from api.models import Offre

class OffreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offre
        fields = '__all__'