from rest_framework import generics
from authentication.serializers.register import ClientRegisterSerializer
from rest_framework.permissions import AllowAny
from users.models.base_user import User

class ClientRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ClientRegisterSerializer
    permission_classes = [AllowAny]