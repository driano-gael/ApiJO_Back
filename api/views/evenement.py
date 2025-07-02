import rest_framework.generics
from api.models.evenement import Evenement
from api.serializers.evenement import EvenementSerializer
from authentication.permissions import *
from rest_framework.permissions import IsAuthenticated, AllowAny


class EvenementListView(rest_framework.generics.ListAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    permission_classes = [AllowAny]

class EvenementDetailView(rest_framework.generics.RetrieveAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    permission_classes = [AllowAny]

class EvenementCreateView(rest_framework.generics.CreateAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class EvenementUpdateView(rest_framework.generics.UpdateAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class EvenementDeleteView(rest_framework.generics.DestroyAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    permission_classes = [IsAuthenticated, IsAdmin]