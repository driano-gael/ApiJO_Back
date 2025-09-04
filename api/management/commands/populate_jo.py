from django.core.management.base import BaseCommand
from api.models import Lieu, Discipline, Epreuve, Evenement
from datetime import date, time, timedelta
import random

class Command(BaseCommand):
    help = 'Peuple la base de données avec des données JO (15 événements minimum)'

    def handle(self, *args, **kwargs):
        if Evenement.objects.exists():
            self.stdout.write(self.style.WARNING("Des données existent déjà. Suppression en cours..."))
            Epreuve.objects.all().delete()
            Evenement.objects.all().delete()
            Discipline.objects.all().delete()
            Lieu.objects.all().delete()

        lieux_noms = [
            "Stade de France", "Accor Arena", "Roland-Garros", "Bercy Arena",
            "Grand Palais", "Château de Versailles", "Paris La Défense Arena",
            "Parc des Princes", "Le Bourget", "Trocadéro"
        ]

        disciplines_data = {
            "Athlétisme": ["100m", "100m femmes", "200m hommes", "200m femmes", "Marathon", "Saut en longueur", "Lancer de poids", "Relais 4x100m", "110m haies", "400m"] ,
            "Natation": ["100m nage libre hommes", "100m nage libre femmes", "200m brasse", "Relais 4x100", "Dos 100m", "Papillon 200m", "400m nage libre", "800m nage libre", "4x200m", "100m papillon"] ,
            "Gymnastique": ["Sol hommes", "Sol femmes", "Barres parallèles", "Barres asymétriques", "Saut de cheval", "Anneaux", "Poutre", "Cheval d'arçon", "Concours général", "Trampoline"] ,
            "Escrime": ["Fleuret hommes", "Fleuret femmes", "Sabre", "Epée", "Individuel", "Par équipe", "Sabre femmes", "Epée hommes", "Fleuret équipe", "Sabre équipe"] ,
            "Judo": ["-60kg hommes", "-48kg femmes", "-66kg", "-52kg", "-73kg", "-57kg", "-81kg", "-63kg", "+100kg", "+78kg"] ,
            "Aviron": ["Deux de couple", "Huit avec barreur", "Quatre sans", "Skiff", "Deux sans barreur", "Quatre de couple", "Skiff femmes", "Skiff hommes", "Poids léger", "Double poids léger"] ,
            "Basketball": ["Match hommes", "Match femmes", "Phase de poule", "Quart de finale", "Demi-finale", "Finale", "3e place", "Basket 3x3", "Basket fauteuil", "Basket mixte"] ,
            "Handball": ["Match hommes", "Match femmes", "Demi-finale", "Finale", "Petite finale", "Handball fauteuil", "Tour préliminaire", "Tour principal", "1/4 de finale", "Handball mixte"] ,
            "Football": ["Match groupe A", "Match groupe B", "Quart de finale", "Demi-finale", "Finale", "Match classement", "Foot féminin", "Foot masculin", "Foot mixte", "Tirs au but"] ,
            "Tennis": ["Simple hommes", "Simple femmes", "Double hommes", "Double femmes", "Double mixte", "1er tour", "2e tour", "1/4 finale", "1/2 finale", "Finale"]
        }

        self.stdout.write("Création des lieux...")
        lieux = [Lieu.objects.create(nom=nom) for nom in lieux_noms]

        self.stdout.write("Création des disciplines et des épreuves...")
        disciplines = {}
        for nom, epreuves in disciplines_data.items():
            discipline = Discipline.objects.create(nom=nom)
            disciplines[nom] = discipline

        date_base = date(2024, 7, 26)
        heure_base = time(10, 0)

        self.stdout.write("Création des événements et association des épreuves...")
        evenement_count = 0
        for nom_disc, discipline in disciplines.items():
            for i in range(0, 10, 2):
                lieu = random.choice(lieux)
                jour = evenement_count % 15
                evenement = Evenement.objects.create(
                    description=f"Événement {nom_disc} #{i//2+1}",
                    date=date_base + timedelta(days=jour),
                    horraire=heure_base,
                    lieu=lieu
                )

                for j in range(2):
                    libelle_epreuve = disciplines_data[nom_disc][i + j]
                    Epreuve.objects.create(
                        libelle=libelle_epreuve,
                        discipline=discipline,
                        evenement=evenement
                    )
                evenement_count += 1

        self.stdout.write(self.style.SUCCESS("Base peuplée avec au moins 15 événements JO !"))