from rest_framework import serializers
from users.models.base_user import User
from users.models.employe import EmployeProfile
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError

class EmployeeRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    nom = serializers.CharField(write_only=True)
    prenom = serializers.CharField(write_only=True)
    identifiant_telephone = serializers.CharField(write_only=True)
    matricule = serializers.CharField(write_only=True)

    class Meta:
        model = EmployeProfile
        # Ici, on liste uniquement les champs qui existent dans EmployeProfile et ceux définis explicitement
        fields = ['email', 'password', 'nom', 'prenom', 'matricule', 'identifiant_telephone']

    def validate_email(self, value):
        # Vérifie si l'email existe déjà
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Un utilisateur avec cet email existe déjà.")
        return value

    def create(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        nom = validated_data.pop('nom')
        prenom = validated_data.pop('prenom')
        matricule = validated_data.pop('matricule')
        identifiant_telephone = validated_data.pop('identifiant_telephone')

        try:
            validate_password(password, user=User(email=email))
        except DjangoValidationError as e:
            raise serializers.ValidationError({'password': e.messages})

        # Création du User avec role 'employe'
        user = User.objects.create_user(
            email=email,
            password=password,
            role='employe'
        )

        # Création du profil employé lié
        employe_profile = EmployeProfile.objects.create(
            user=user,
            nom=nom,
            prenom=prenom,
            matricule=matricule,
            identifiant_telephone=identifiant_telephone
        )
        return employe_profile
