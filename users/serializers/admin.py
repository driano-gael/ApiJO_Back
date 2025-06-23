from rest_framework import serializers
from users.models.admin import AdminProfile

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminProfile
        fields = ['id', 'user', 'nom', 'prenom', 'matricule']
        read_only_fields = ['id', 'user']