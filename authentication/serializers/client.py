"""
Sérialiseurs pour l'inscription des clients.

Ce module contient le(s) sérialiseur(s) permettant de gérer l'inscription
des clients. Il inclut la validation des données d'entrée (email, mot de passe,
nom, prénom, téléphone) et la création automatique du profil client associé à l'utilisateur.
"""

from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from authentication.validators.emailValidator import EmailValidator

from users.models.base_user import User
from users.models.client import ClientProfile


class ClientRegisterSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour l'inscription des clients.

    Gère l'enregistrement complet d'un client, y compris :
        - validation de l'email (unicité et format),
        - validation du mot de passe (Django),
        - validation du nom et prénom (≥2 caractères),
        - validation du téléphone (≥10 chiffres),
        - création de l'utilisateur et du profil client associé.

    :field email: Adresse email unique du client.
    :type email: str
    :field password: Mot de passe sécurisé.
    :type password: str
    :field nom: Nom de famille.
    :type nom: str
    :field prenom: Prénom.
    :type prenom: str
    :field telephone: Numéro de téléphone.
    :type telephone: str
    """

    email = serializers.EmailField(write_only=True, validators=[EmailValidator()])
    nom = serializers.CharField(write_only=True)
    prenom = serializers.CharField(write_only=True)
    telephone = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'nom', 'prenom', 'telephone']

    def validate_email(self, value):
        """
        Vérifie que l'email n'est pas déjà utilisé.

        :param value: Email à valider.
        :type value: str
        :raises serializers.ValidationError: Si l'email existe déjà.
        :return: L'email validé.
        :rtype: str
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Cet email est déjà utilisé.")
        return value

    def validate_password(self, value):
        """
        Applique la validation sécurisée de Django sur le mot de passe.

        :param value: Mot de passe à valider.
        :type value: str
        :raises serializers.ValidationError: Si le mot de passe ne respecte pas les critères de sécurité.
        :return: Le mot de passe validé.
        :rtype: str
        """
        try:
            validate_password(value, user=User(email=self.initial_data.get('email')))
        except DjangoValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value

    def validate_nom(self, value):
        """
        Vérifie que le nom contient au moins 2 caractères.

        :param value: Nom à valider.
        :type value: str
        :raises serializers.ValidationError: Si le nom est trop court.
        :return: Nom validé.
        :rtype: str
        """
        if len(value) < 2:
            raise serializers.ValidationError("Le nom doit contenir au moins 2 caractères.")
        return value

    def validate_prenom(self, value):
        """
        Vérifie que le prénom contient au moins 2 caractères.

        :param value: Prénom à valider.
        :type value: str
        :raises serializers.ValidationError: Si le prénom est trop court.
        :return: Prénom validé.
        :rtype: str
        """
        if len(value) < 2:
            raise serializers.ValidationError("Le prénom doit contenir au moins 2 caractères.")
        return value

    def validate_telephone(self, value):
        """
        Vérifie que le numéro de téléphone contient au moins 10 chiffres et est numérique.

        :param value: Numéro de téléphone à valider.
        :type value: str
        :raises serializers.ValidationError: Si le numéro est invalide.
        :return: Numéro de téléphone validé.
        :rtype: str
        """
        if not value.isdigit() or len(value) < 10:
            raise serializers.ValidationError("Le numéro de téléphone doit contenir au moins 10 chiffres.")
        return value

    def create(self, validated_data):
        """
        Crée un utilisateur et son profil client associé.

        :param validated_data: Données validées par le sérialiseur.
        :type validated_data: dict
        :return: Instance de l'utilisateur créé.
        :rtype: User
        """
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
