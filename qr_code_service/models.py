from django.db import models
from api.models import Ticket


class QrCode(models.Model):
    data = models.TextField(help_text="Données encodées dans le QR code")
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE, related_name='qrcodes', help_text="Ticket associé à ce QR code")
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"QR Code {self.id} - {self.data}"