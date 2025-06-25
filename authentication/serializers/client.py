from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
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
        password = validated_data.pop('password')
        email = validated_data['email']

        try:
            validate_password(password, user=User(email=email))
        except DjangoValidationError as e:
            raise serializers.ValidationError({'password': e.messages})

        user = User.objects.create_user(
            email=email,
            password=password,
            role='client'
        )
        ClientProfile.objects.create(user=user, nom=nom, prenom=prenom, telephone=telephone)
        return user
