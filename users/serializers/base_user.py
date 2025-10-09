"""
Sérialiseur pour le modèle utilisateur personnalisé.

Ce module définit la sérialisation/désérialisation des objets User
pour l'API REST, avec gestion sécurisée des mots de passe.
"""

from rest_framework import serializers
from users.models.base_user import User


class UserSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle User.

    :ivar id: Identifiant unique de l'utilisateur (lecture seule)
    :vartype id: int
    :ivar email: Adresse email unique
    :vartype email: str
    :ivar password: Mot de passe en clair pour création/mise à jour (écriture seule)
    :vartype password: str
    :ivar role: Rôle de l'utilisateur (client, employe, admin)
    :vartype role: str
    """
    password = serializers.CharField(write_only=True, required=True, min_length=8)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'role', 'is_active', 'date_joined']
        read_only_fields = ['id']

    def create(self, validated_data):
        """
        Crée un nouvel utilisateur avec mot de passe sécurisé.

        :param validated_data: Données validées du serializer
        :type validated_data: dict
        :return: Instance User créée
        :rtype: User
        """
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        """
        Met à jour un utilisateur existant et modifie le mot de passe si fourni.

        :param instance: Instance User à mettre à jour
        :type instance: User
        :param validated_data: Données validées du serializer
        :type validated_data: dict
        :return: Instance User mise à jour
        :rtype: User
        """
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
