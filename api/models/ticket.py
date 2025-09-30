import hashlib

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
    key = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        """
        Sauvegarde le ticket et génère une clé unique incluant l'ID.

        La clé est calculée après l'insertion initiale pour inclure self.id,
        garantissant l'unicité absolue.
        """
        # Sauvegarde initiale pour générer l'ID si nécessaire
        if not self.id:
            super().save(*args, **kwargs)

        if not self.key:
            raw_key = f"{self.client.cle_chiffree}-{self.date_achat}-{self.id}"
            self.key = hashlib.sha256(raw_key.encode('utf-8')).hexdigest()
            super().save(*args, **kwargs)

    def __str__(self):
        return f"Ticket {self.id} - {self.evenement} - {self.client.nom}"

    class Meta:
        ordering = ['-date_achat']