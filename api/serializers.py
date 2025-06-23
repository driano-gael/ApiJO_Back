from rest_framework import serializers
from .models import Lieu



class LieuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lieu
        fields = '__all__'

class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lieu
        fields = '__all__'