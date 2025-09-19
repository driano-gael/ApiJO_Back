from django.core.management.base import BaseCommand
from users.models.base_user import User
from users.models.admin import AdminProfile
from django.conf import settings
import os

class Command(BaseCommand):
    help = "Créer un utilisateur admin sans superuser"

    def handle(self, *args, **kwargs):
        try:
            # Récupération des variables d'environnement
            email = os.getenv('ADMIN_EMAIL', 'admin@admin.com')
            password = os.getenv('ADMIN_PASSWORD', '@DminPass123')
            nom = os.getenv('ADMIN_NOM', 'Admin')
            prenom = os.getenv('ADMIN_PRENOM', 'admin')
            matricule = os.getenv('ADMIN_MATRICULE', 'ADM001')

            if User.objects.filter(email=email).exists():
                self.stdout.write(self.style.WARNING("L'utilisateur admin existe déjà."))
                return

            user = User.objects.create_user(
                email=email,
                password=password,
                role='admin',
                is_staff=True  # important pour les permissions admin
            )

            AdminProfile.objects.create(
                user=user,
                nom=nom,
                prenom=prenom,
                matricule=matricule
            )

            self.stdout.write(self.style.SUCCESS(f"Admin créé avec succès : {email}"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Erreur : {e}"))
