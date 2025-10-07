import qrcode
from io import BytesIO
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from qr_code_service.models import QrCode
from .serializers import QRCodeSerializer, TicketIdSerializer
from api.models import Ticket


class QRCodeCreateByTicket(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QRCodeSerializer


    @extend_schema(
        request=TicketIdSerializer,
        responses=QRCodeSerializer
    )
    def post(self, request):
        ticket_id = request.data.get('ticket_id')
        if not ticket_id:
            return Response({'message': 'ticket_id requis'}, status=400)
        try:
            ticket = Ticket.objects.get(id=ticket_id)
        except Ticket.DoesNotExist:
            return Response({'message': 'ticket_id invalide'}, status=status.HTTP_400_BAD_REQUEST)

        if ticket.client != request.user.client_profile:
            return Response(
                {'message': "Vous n'êtes pas autorisé à accéder à ce ticket."},
                status=status.HTTP_403_FORBIDDEN
            )

        qr_code = QrCode.objects.filter(ticket_id=ticket_id).first()
        if qr_code:
            serializer = QRCodeSerializer(qr_code)
            return Response(serializer.data, status=200)

        qr_image = qrcode.make(ticket.key)
        buffer = BytesIO()
        qr_image.save(buffer, format="PNG")
        qr_data = buffer.getvalue()


        qrcode_obj = QrCode.objects.create(
            ticket=ticket,
            data=qr_data
        )

        serializer = QRCodeSerializer(qrcode_obj)
        return Response(serializer.data, status=status.HTTP_201_CREATED)