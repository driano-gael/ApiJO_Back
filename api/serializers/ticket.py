from rest_framework import serializers
from api.models import Ticket
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
    evenementId = serializers.IntegerField()
    offreId = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)

    def validate_offreId(self, value):
        from api.models import Offre
        if not Offre.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Offre introuvable.")
        return value