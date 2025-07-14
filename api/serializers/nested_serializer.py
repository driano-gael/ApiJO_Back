from rest_framework import serializers
from api.models.epreuve import Epreuve
from api.models.evenement import Evenement

class NestedEpreuveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Epreuve
        fields = ['id', 'libelle']

class NestedEvenementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evenement
        fields = ['id', 'description']