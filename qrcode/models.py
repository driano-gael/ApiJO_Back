from django.db import models
from api.models import Ticket


class QrCode(models.Model):
    data = models.CharField(max_length=255, help_text="Données encodées dans le QR code")
    image = models.ImageField(upload_to='qrcodes/', help_text="Image du QR code généré")
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='qrcodes', help_text="Ticket associé à ce QR code")

    def __str__(self):
        return f"QR Code {self.id} - {self.data}"