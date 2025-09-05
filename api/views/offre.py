import rest_framework.generics
from api.models import Offre
from api.serializers import OffreSerializer
from authentication.permissions import *
from rest_framework.permissions import IsAuthenticated, AllowAny


class OffreListView(rest_framework.generics.ListAPIView):
    queryset = Offre.objects.order_by("nb_personne", "montant")
    serializer_class = OffreSerializer
    permission_classes = [AllowAny]

class OffreDetailView(rest_framework.generics.RetrieveAPIView):
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer
    permission_classes = [AllowAny]

class OffreCreateView(rest_framework.generics.CreateAPIView):
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class OffreUpdateView(rest_framework.generics.UpdateAPIView):
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class OffreDeleteView(rest_framework.generics.DestroyAPIView):
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer
    permission_classes = [IsAuthenticated, IsAdmin]