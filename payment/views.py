from django.db import transaction
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from api.serializers import TicketSerializer
from .serializers import MockPaymentRequestSerializer, MockPaymentResponseSerializer
from .services.payment_service import PaymentService
from .services.ticket_service import TicketService


class MockPaymentView(APIView):
    """
    Endpoint POST /api/payments/check/
    Simule un appel a un service de paiement.
    """
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=MockPaymentRequestSerializer,
        responses=MockPaymentResponseSerializer,
        tags=['Paiement']
    )

    def post(self, request):
        serializer = MockPaymentRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        amount = data["amount"]
        force_failed = data.get("force_failed", False)
        items = data.get("items", [])

        payment_service = PaymentService()

        # 1️⃣ Création du PaymentIntent
        payment_intent = payment_service.create_payment_intent(amount, force_failed)

        response_data = {
            "success": False,
            "gateway_response": payment_intent,
            "tickets": [],
            "errors": []
        }

        tickets = []
        if payment_intent["status"] == "requires_confirmation" and items:
            try:
                with transaction.atomic():
                    tickets = TicketService.create_tickets_from_items(
                        request.user.client_profile,
                        items
                    )

                # Confirmation du paiement
                confirmed = payment_service.confirm_payment(payment_intent["transaction_id"])
                response_data["success"] = True
                response_data["gateway_response"] = confirmed


            except ValueError as e:
                refund = payment_service.refund(payment_intent["transaction_id"])
                response_data["errors"].append({"reason": str(e)})
                response_data["gateway_response"] = refund

        response_data["tickets"] = TicketSerializer(tickets, many=True).data
        response_serializer = MockPaymentResponseSerializer(response_data)
        return Response(response_serializer.data, status=status.HTTP_200_OK)
