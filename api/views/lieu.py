import rest_framework.generics
from api.models import Lieu
from api.serializers import LieuSerializer
from authentication.permissions import *
from rest_framework.permissions import IsAuthenticated, AllowAny


class LieuListView(rest_framework.generics.ListAPIView):
    queryset = Lieu.objects.all()
    serializer_class = LieuSerializer
    permission_classes = [AllowAny]

class LieuDetailView(rest_framework.generics.RetrieveAPIView):
    queryset = Lieu.objects.all()
    serializer_class = LieuSerializer
    permission_classes = [AllowAny]

class LieuCreateView(rest_framework.generics.CreateAPIView):
    queryset = Lieu.objects.all()
    serializer_class = LieuSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class LieuUpdateView(rest_framework.generics.UpdateAPIView):
    queryset = Lieu.objects.all()
    serializer_class = LieuSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class LieuDeleteView(rest_framework.generics.DestroyAPIView):
    queryset = Lieu.objects.all()
    serializer_class = LieuSerializer
    permission_classes = [IsAuthenticated, IsAdmin]