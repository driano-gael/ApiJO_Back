from rest_framework import serializers
from api.models import Evenement

class EvenementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evenement
        fields = '__all__'