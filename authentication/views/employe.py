from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from authentication.serializers.employee import EmployeeRegisterSerializer
from users.models.employe import EmployeProfile

class EmployeeRegisterView(generics.CreateAPIView):
    queryset = EmployeProfile.objects.all()
    serializer_class = EmployeeRegisterSerializer
    permission_classes = [IsAdminUser]