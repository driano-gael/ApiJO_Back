"""
Sérialiseurs pour l'inscription des employés.

Ce module contient les sérialiseurs nécessaires pour gérer l'inscription
des employés avec validation des données et création automatique du profil.

:module: users.serializers.employee_register
"""

from rest_framework import serializers
from users.models.base_user import User
from users.models.employe import EmployeProfile
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError

class EmployeeRegisterSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour l'inscription des employés.

    Gère l'inscription complète d'un employé avec création automatique
    du profil utilisateur et validation de tous les champs requis.

    :ivar email: Adresse email unique
    :type email: str
    :ivar password: Mot de passe (avec validation Django)
    :type password: str
    :ivar nom: Nom de famille
    :type nom: str
    :ivar prenom: Prénom
    :type prenom: str
    :ivar matricule: Numéro de matricule employé (unique)
    :type matricule: str
    :ivar identifiant_telephone: Identifiant téléphonique professionnel
    :type identifiant_telephone: str
    """
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    nom = serializers.CharField(write_only=True)
    prenom = serializers.CharField(write_only=True)
    identifiant_telephone = serializers.CharField(write_only=True)
    matricule = serializers.CharField(write_only=True)

    class Meta:
        """
        Configuration du sérialiseur.

        :cvar model: Modèle Django associé au sérialiseur
        :type model: EmployeProfile
        :cvar fields: Champs inclus dans la sérialisation
        :type fields: list
        """
        model = EmployeProfile
        fields = ['email', 'password', 'nom', 'prenom', 'matricule', 'identifiant_telephone']

    def validate_email(self, value):
        """
        Valide l'unicité de l'adresse email.

        :param value: L'adresse email à valider
        :type value: str
        :return: L'email validé
        :rtype: str
        :raises serializers.ValidationError: Si l'email est déjà utilisé
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Un utilisateur avec cet email existe déjà.")
        return value

    def create(self, validated_data):
        """
        Crée un nouvel utilisateur employé avec son profil.

        Valide le mot de passe selon les règles Django et crée l'utilisateur
        avec le rôle 'employe' ainsi que son profil associé.

        :param validated_data: Les données validées
        :type validated_data: dict
        :return: Le profil employé créé
        :rtype: EmployeProfile
        :raises serializers.ValidationError: Si le mot de passe ne respecte pas les règles
        """
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

        employe_profile = EmployeProfile.objects.create(
            user=user,
            nom=nom,
            prenom=prenom,
            matricule=matricule,
            identifiant_telephone=identifiant_telephone
        )
        return employe_profile
