from rest_framework import serializers
from api.models import Discipline



class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'