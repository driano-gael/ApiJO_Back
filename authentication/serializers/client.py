from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from authentication.validators.emailValidator import EmailValidator

from users.models.base_user import User
from users.models.client import ClientProfile

class ClientRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True, validators=[EmailValidator()])
    nom = serializers.CharField(write_only=True)
    prenom = serializers.CharField(write_only=True)
    telephone = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'nom', 'prenom', 'telephone']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Cet email est déjà utilisé.")
        return value

    def validate_password(self, value):
        try:
            validate_password(value, user=User(email=self.initial_data.get('email')))
        except DjangoValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value

    def validate_nom(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Le nom doit contenir au moins 2 caractères.")
        return value

    def validate_prenom(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Le prénom doit contenir au moins 2 caractères.")
        return value

    def validate_telephone(self, value):
        if not value.isdigit() or len(value) < 10:
            raise serializers.ValidationError("Le numéro de téléphone doit contenir au moins 10 chiffres.")
        return value

    def create(self, validated_data):
        nom = validated_data.pop('nom')
        prenom = validated_data.pop('prenom')
        telephone = validated_data.pop('telephone')
        password = validated_data.pop('password')
        email = validated_data['email']

        user = User.objects.create_user(
            email=email,
            password=password,
            role='client'
        )
        ClientProfile.objects.create(user=user, nom=nom, prenom=prenom, telephone=telephone)
        return user
