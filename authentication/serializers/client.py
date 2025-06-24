from rest_framework import serializers
from users.models.base_user import User
from users.models.client import ClientProfile

class ClientRegisterSerializer(serializers.ModelSerializer):
    nom = serializers.CharField(write_only=True)
    prenom = serializers.CharField(write_only=True)
    telephone = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'nom', 'prenom', 'telephone']

    def create(self, validated_data):
        nom = validated_data.pop('nom')
        prenom = validated_data.pop('prenom')
        telephone = validated_data.pop('telephone')
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            role='client'
        )
        ClientProfile.objects.create(user=user, nom=nom, prenom=prenom, telephone=telephone)
        return user