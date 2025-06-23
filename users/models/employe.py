from django.db import models
from .base_user import User

class EmployeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employe_profile')
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    matricule = models.CharField(max_length=50)
    identifiant_telephone = models.CharField(max_length=255)