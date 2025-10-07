import json
from io import BytesIO

from django.core.files.base import ContentFile
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated

from qrcode import make
from rest_framework.views import APIView
from api.models import Ticket
from qr_code_service.models import QrCode
from .serializers import QRCodeSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class QRCodeCreateByTicket(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QRCodeSerializer


    @extend_schema(
        request="ticket_id: integer",
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

        qr_data = {'ticket_key': ticket.key}
        qr_image = make(qr_data)
        buffer = BytesIO()
        qr_image.save(buffer, format='PNG')
        data=json.dumps(qr_data)

        qrcode_obj = QrCode.objects.create(
            ticket=ticket,
            data=data
        )

        serializer = QRCodeSerializer(qrcode_obj)
        return Response(serializer.data, status=status.HTTP_201_CREATED)