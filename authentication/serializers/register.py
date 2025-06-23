from rest_framework import serializers
from users.models.base_user import User
from users.models.client import ClientProfile

class ClientRegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    phone = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'phone']

    def create(self, validated_data):
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        phone = validated_data.pop('phone')
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            role='client'
        )
        ClientProfile.objects.create(user=user, first_name=first_name, last_name=last_name, phone=phone)
        return user
