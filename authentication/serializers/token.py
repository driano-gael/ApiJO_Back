from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import serializers
from users.models.base_user import User as CustomUser

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise serializers.ValidationError("Identifiants invalides.")
            assert isinstance(user, CustomUser)
        else:
            raise serializers.ValidationError("Email et mot de passe requis.")

        data = super().validate(attrs)
        data['role'] = user.role
        data['email'] = user.email
        return data
