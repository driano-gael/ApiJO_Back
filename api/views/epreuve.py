import rest_framework.generics
from api.models.epreuve import Epreuve
from api.serializers.epreuve import EpreuveSerializer
from authentication.permissions import *
from rest_framework.permissions import IsAuthenticated, AllowAny


class EpreuveListView(rest_framework.generics.ListAPIView):
    queryset = Epreuve.objects.select_related("evenement", "discipline").order_by(
        "discipline__nom","evenement__date", "evenement__horraire"
    )
    serializer_class = EpreuveSerializer
    permission_classes = [AllowAny]

class EpreuveDetailView(rest_framework.generics.RetrieveAPIView):
    queryset = Epreuve.objects.all()
    serializer_class = EpreuveSerializer
    permission_classes = [AllowAny]

class EpreuveCreateView(rest_framework.generics.CreateAPIView):
    queryset = Epreuve.objects.all()
    serializer_class = EpreuveSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class EpreuveUpdateView(rest_framework.generics.UpdateAPIView):
    queryset = Epreuve.objects.all()
    serializer_class = EpreuveSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class EpreuveDeleteView(rest_framework.generics.DestroyAPIView):
    queryset = Epreuve.objects.all()
    serializer_class = EpreuveSerializer
    permission_classes = [IsAuthenticated, IsAdmin]