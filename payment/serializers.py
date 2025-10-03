from rest_framework import serializers

from api.serializers import PanierItemSerializer, TicketSerializer


class MockPaymentRequestSerializer(serializers.Serializer):
    """
    Sérialiseur de la requête de paiement mock.
    On attend :
    - amount : montant total
    - force_failed : booléen pour simuler un échec
    - items : liste des éléments du panier (offre, événement, quantité)
    """
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    force_failed = serializers.BooleanField(required=False, default=False)
    items = PanierItemSerializer(many=True, required=False)


class MockPaymentResponseSerializer(serializers.Serializer):
    """
    Sérialiseur de la réponse du paiement mock.
    On renvoie :
    - success : booléen succès/échec
    - gateway_response : réponse brute de la passerelle
    - tickets : liste des tickets créés (si paiement réussi)
    - errors : liste des erreurs éventuelles
    """
    success = serializers.BooleanField()
    gateway_response = serializers.DictField()
    tickets = TicketSerializer(many=True, required=False)
    errors = serializers.ListField(
        child=serializers.DictField(), required=False
    )