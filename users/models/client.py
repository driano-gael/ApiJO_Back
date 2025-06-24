import hashlib
from django.db import models
from .base_user import User

class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    cle_chiffree = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.cle_chiffree:
            raw_key = f"{self.user.email}-{self.nom}"
            self.cle_chiffree = hashlib.sha256(raw_key.encode('utf-8')).hexdigest()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nom} {self.prenom}"