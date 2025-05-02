from django.core.management.base import BaseCommand
from api.models import Lieu
from faker import Faker

class Command(BaseCommand):
    help = 'Génère des lieux fictifs avec Faker'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Nombre de lieux à créer')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        faker = Faker('fr_FR')  # pour des villes françaises

        for _ in range(total):
            nom = faker.company() + ' Arena'
            lieu = Lieu(nom=nom)
            lieu.save()

        self.stdout.write(self.style.SUCCESS(f'{total} lieux créés avec succès !'))