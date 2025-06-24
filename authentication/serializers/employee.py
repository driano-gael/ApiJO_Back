from rest_framework import serializers
from users.models.base_user import User
from users.models.employe import EmployeProfile # modèle étendu

class EmployeeRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = EmployeProfile
        fields = ['email', 'password', 'first_name', 'last_name', 'matricule', 'device_id']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            role='employe'
        )
        employee = EmployeProfile.objects.create(
            user=user,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            matricule=validated_data['matricule'],
            device_id=validated_data['device_id']
        )
        return employee