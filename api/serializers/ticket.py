from rest_framework import serializers
from api.models import Ticket, Offre, Evenement
from api.serializers import OffreSerializer
from api.serializers.nested_serializer import NestedEvenementSerializer
from users.serializers import ClientSerializer


class TicketSerializer(serializers.ModelSerializer):

    offre = OffreSerializer(read_only=True)
    evenement = NestedEvenementSerializer(read_only=True)
    client = ClientSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'


class PanierItemSerializer(serializers.Serializer):
    offreId = serializers.PrimaryKeyRelatedField(queryset=Offre.objects.all(), source="offre")
    evenementId = serializers.PrimaryKeyRelatedField(queryset=Evenement.objects.all(), source="evenement")
    quantity = serializers.IntegerField(min_value=1)