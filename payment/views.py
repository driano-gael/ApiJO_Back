from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.conf import settings

from .infrastructure.payement_gateway import StripeGatewayMock
from .serializers import MockPaymentRequestSerializer, MockPaymentResponseSerializer

class MockStripePaymentView(APIView):
    """
    Endpoint POST /api/payments/mock-stripe/
    Simule un appel Stripe (PaymentIntent.create).
    """
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=MockPaymentRequestSerializer,
        responses=MockPaymentResponseSerializer,
        tags=['Paiement']
    )

    def post(self, request):
        # Validation de la requête
        serializer = MockPaymentRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        amount = data["amount"]
        force_failed = data.get("force_failed")

        gateway = StripeGatewayMock()
        result = gateway.create_payment_intent(amount, force_failed)

        response_data = {
            "success": result["status"] == "succeeded",
            "gateway_response": result
        }

        response_serializer = MockPaymentResponseSerializer(response_data)

        return Response(response_serializer.data, status=status.HTTP_200_OK)
