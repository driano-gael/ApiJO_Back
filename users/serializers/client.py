from rest_framework import serializers
from users.models.client import ClientProfile

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = ['id', 'user', 'nom', 'prenom', 'telephone', 'cle_chiffree']
        read_only_fields = ['id', 'user', 'cle_chiffree']

    def create(self, validated_data):
        # la clé chiffrée est générée dans le modèle lors du save()
        return super().create(validated_data)