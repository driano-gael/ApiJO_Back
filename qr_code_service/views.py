import base64

import qrcode
from io import BytesIO
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from api.serializers import TicketSerializer
from authentication.permissions import IsAdminOrEmploye
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
        qr_data = base64.b64encode(buffer.getvalue()).decode('utf-8')


        qrcode_obj, created = QrCode.objects.get_or_create(
            ticket=ticket,
            data=qr_data
        )

        serializer = QRCodeSerializer(qrcode_obj)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class TicketByKeyView(APIView):
    """
    Vue qui reçoit une clé de ticket (key) et renvoie le ticket correspondant.
    Accessible uniquement aux employés authentifiés.
    """
    permission_classes = [IsAdminOrEmploye]

    @extend_schema(
        request=None,
        responses=TicketSerializer,
        description="Récupère un ticket à partir de sa clé QR"
    )
    def get(self, request, key):
        try:
            ticket = Ticket.objects.get(key=key)
        except Ticket.DoesNotExist:
            return Response(
                {"message": "Ticket introuvable"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = TicketSerializer(ticket)
        return Response(serializer.data, status=status.HTTP_200_OK)