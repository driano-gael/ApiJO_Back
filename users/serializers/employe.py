from rest_framework import serializers
from users.models.employe import EmployeProfile

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeProfile
        fields = ['id', 'user', 'nom', 'prenom', 'matricule', 'identifiant_telephone']
        read_only_fields = ['id', 'user']