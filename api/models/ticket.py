from django.db import models
from users.models import ClientProfile

class Ticket(models.Model):
    STATUT_CHOICES = [
        ('valide', 'Valide'),
        ('invalide ', 'Invalide')]

    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    evenement = models.ForeignKey('Evenement', on_delete=models.CASCADE)
    offre = models.ForeignKey('Offre', on_delete=models.CASCADE)
    date_achat = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='valide')
    qr_code = models.CharField(max_length=255, unique=True)
    key = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"Ticket {self.id} - {self.evenement} - {self.client.nom}"

    class Meta:
        ordering = ['-date_achat']