import random
from datetime import date, time, timedelta

from django.core.management.base import BaseCommand

from api.models import Lieu, Discipline, Epreuve, Evenement


class Command(BaseCommand):
    help = 'Peuple la base de données avec des données JO (15 événements minimum)'

    def date_aleatoire(self):
        date_start = date(2024, 7, 26)
        delta = date(2024, 10, 10) - date_start
        jours_aleatoires = random.randint(0, delta.days)
        return date_start + timedelta(days=jours_aleatoires)

    # Fonction utilitaire pour générer une heure aléatoire entre 10h et 17h
    def heure_aleatoire(self):
        heure = random.randint(10, 16)
        minute = random.randint(0, 59)
        return time(hour=heure, minute=minute)

    def handle(self, *args, **kwargs):
        # Nettoyage
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

        # ➡️ Nouvelle structure de données
        disciplines_data = {
            "Athlétisme": [
                {"libelle": "100m", "genre": "hommes", "tour": "finale"},
                {"libelle": "100m", "genre": "femmes", "tour": "finale"},
                {"libelle": "200m", "genre": "hommes", "tour": "demi-finale"},
                {"libelle": "200m", "genre": "femmes", "tour": "demi-finale"},
                {"libelle": "400m", "genre": "hommes", "tour": "demi-finale"},
                {"libelle": "400m", "genre": "femmes", "tour": "demi-finale"},
                {"libelle": "Relais 4x100m", "genre": "hommes", "tour": "finale"},
                {"libelle": "Relais 4x100m", "genre": "femmes", "tour": "finale"},
                {"libelle": "Saut en longueur", "genre": "hommes", "tour": "qualification"},
                {"libelle": "Saut en longueur", "genre": "femmes", "tour": "qualification"}
            ],
            "Football": [
                {"libelle": "Match de groupe", "genre": "hommes", "tour": "groupe"},
                {"libelle": "Match de groupe", "genre": "femmes", "tour": "groupe"},
                {"libelle": "Quart de finale", "genre": "hommes", "tour": "quart"},
                {"libelle": "Quart de finale", "genre": "femmes", "tour": "quart"},
                {"libelle": "Demi-finale", "genre": "hommes", "tour": "demi"},
                {"libelle": "Demi-finale", "genre": "femmes", "tour": "demi"},
                {"libelle": "Finale", "genre": "hommes", "tour": "finale"},
                {"libelle": "Finale", "genre": "femmes", "tour": "finale"},
                {"libelle": "Match", "genre": "hommes", "tour": "classement"},
                {"libelle": "Tirs au but", "genre": "mixte", "tour": "finale"}
            ],
            "Natation": [
                {"libelle": "100m nage libre", "genre": "hommes", "tour": "séries"},
                {"libelle": "100m nage libre", "genre": "femmes", "tour": "séries"},
                {"libelle": "200m brasse", "genre": "hommes", "tour": "demi-finale"},
                {"libelle": "200m brasse", "genre": "femmes", "tour": "demi-finale"},
                {"libelle": "400m nage libre", "genre": "hommes", "tour": "finale"},
                {"libelle": "400m nage libre", "genre": "femmes", "tour": "finale"},
                {"libelle": "Relais 4x100", "genre": "hommes", "tour": "finale"},
                {"libelle": "Relais 4x100", "genre": "femmes", "tour": "finale"},
                {"libelle": "Papillon 200m", "genre": "hommes", "tour": "demi-finale"},
                {"libelle": "Papillon 200m", "genre": "femmes", "tour": "demi-finale"}
            ],
            "Gymnastique": [
                {"libelle": "Sol", "genre": "hommes", "tour": "finale"},
                {"libelle": "Sol", "genre": "femmes", "tour": "finale"},
                {"libelle": "Barres parallèles", "genre": "hommes", "tour": "finale"},
                {"libelle": "Barres asymétriques", "genre": "femmes", "tour": "finale"},
                {"libelle": "Saut de cheval", "genre": "hommes", "tour": "finale"},
                {"libelle": "Poutre", "genre": "femmes", "tour": "finale"},
                {"libelle": "Anneaux", "genre": "hommes", "tour": "finale"},
                {"libelle": "Cheval d'arçon", "genre": "hommes", "tour": "finale"},
                {"libelle": "Concours général", "genre": "mixte", "tour": "finale"},
                {"libelle": "Trampoline", "genre": "mixte", "tour": "finale"}
            ],
            "Escrime": [
                {"libelle": "Fleuret", "genre": "hommes", "tour": "finale"},
                {"libelle": "Fleuret", "genre": "femmes", "tour": "finale"},
                {"libelle": "Sabre", "genre": "hommes", "tour": "demi"},
                {"libelle": "Sabre", "genre": "femmes", "tour": "demi"},
                {"libelle": "Epée", "genre": "hommes", "tour": "finale"},
                {"libelle": "Epée", "genre": "femmes", "tour": "finale"},
                {"libelle": "Individuel", "genre": "hommes", "tour": "qualification"},
                {"libelle": "Individuel", "genre": "femmes", "tour": "qualification"},
                {"libelle": "Par équipe", "genre": "hommes", "tour": "finale"},
                {"libelle": "Par équipe", "genre": "femmes", "tour": "finale"}
            ],
            "Judo": [
                {"libelle": "-60kg", "genre": "hommes", "tour": "finale"},
                {"libelle": "-48kg", "genre": "femmes", "tour": "finale"},
                {"libelle": "-66kg", "genre": "hommes", "tour": "demi"},
                {"libelle": "-52kg", "genre": "femmes", "tour": "demi"},
                {"libelle": "-73kg", "genre": "hommes", "tour": "finale"},
                {"libelle": "-57kg", "genre": "femmes", "tour": "finale"},
                {"libelle": "-81kg", "genre": "hommes", "tour": "finale"},
                {"libelle": "-63kg", "genre": "femmes", "tour": "finale"},
                {"libelle": "+100kg", "genre": "hommes", "tour": "finale"},
                {"libelle": "+78kg", "genre": "femmes", "tour": "finale"}
            ],
            "Aviron": [
                {"libelle": "Deux de couple", "genre": "hommes", "tour": "finale"},
                {"libelle": "Huit avec barreur", "genre": "hommes", "tour": "finale"},
                {"libelle": "Quatre sans", "genre": "hommes", "tour": "finale"},
                {"libelle": "Skiff", "genre": "hommes", "tour": "finale"},
                {"libelle": "Deux sans barreur", "genre": "hommes", "tour": "finale"},
                {"libelle": "Quatre de couple", "genre": "hommes", "tour": "finale"},
                {"libelle": "Skiff", "genre": "femmes", "tour": "finale"},
                {"libelle": "Poids léger", "genre": "hommes", "tour": "finale"},
                {"libelle": "Poids léger", "genre": "femmes", "tour": "finale"},
                {"libelle": "Double poids léger", "genre": "mixte", "tour": "finale"}
            ],
            "Tir à l'arc": [
                {"libelle": "Tir à 70m", "genre": "hommes", "tour": "qualification"},
                {"libelle": "Tir à 70m", "genre": "femmes", "tour": "qualification"},
                {"libelle": "Match à élimination directe", "genre": "hommes", "tour": "1/16"},
                {"libelle": "Match à élimination directe", "genre": "femmes", "tour": "1/16"},
                {"libelle": "Quart de finale", "genre": "hommes", "tour": "quart"},
                {"libelle": "Quart de finale", "genre": "femmes", "tour": "quart"},
                {"libelle": "Demi-finale", "genre": "hommes", "tour": "demi"},
                {"libelle": "Demi-finale", "genre": "femmes", "tour": "demi"},
                {"libelle": "Finale", "genre": "hommes", "tour": "finale"},
                {"libelle": "Finale", "genre": "femmes", "tour": "finale"}
            ],
            "Volley-ball": [
                {"libelle": "Match de poule", "genre": "hommes", "tour": "poule"},
                {"libelle": "Match de poule", "genre": "femmes", "tour": "poule"},
                {"libelle": "Quart de finale", "genre": "hommes", "tour": "quart"},
                {"libelle": "Quart de finale", "genre": "femmes", "tour": "quart"},
                {"libelle": "Demi-finale", "genre": "hommes", "tour": "demi"},
                {"libelle": "Demi-finale", "genre": "femmes", "tour": "demi"},
                {"libelle": "Finale", "genre": "hommes", "tour": "finale"},
                {"libelle": "Finale", "genre": "femmes", "tour": "finale"},
                {"libelle": "Volley 3x3", "genre": "mixte", "tour": "finale"},
                {"libelle": "Volley fauteuil", "genre": "mixte", "tour": "finale"}
            ],
            "Tennis": [
                {"libelle": "Simple", "genre": "hommes", "tour": "1er tour"},
                {"libelle": "Simple", "genre": "femmes", "tour": "1er tour"},
                {"libelle": "Double", "genre": "hommes", "tour": "demi"},
                {"libelle": "Double", "genre": "femmes", "tour": "demi"},
                {"libelle": "Double", "genre": "mixte", "tour": "demi"},
                {"libelle": "2e tour", "genre": "mixte", "tour": "2e tour"},
                {"libelle": "1/4 finale", "genre": "mixte", "tour": "quart"},
                {"libelle": "1/2 finale", "genre": "mixte", "tour": "demi"},
                {"libelle": "Simple", "genre": "hommes", "tour": "finale"},
                {"libelle": "Simple", "genre": "femmes", "tour": "finale"}
            ]
        }

        self.stdout.write("Création des lieux...")
        lieux = [Lieu.objects.create(nom=nom) for nom in lieux_noms]

        self.stdout.write("Création des disciplines...")
        disciplines = {}
        for nom in disciplines_data.keys():
            discipline = Discipline.objects.create(nom=nom)
            disciplines[nom] = discipline

        self.stdout.write("Création des événements et épreuves...")

        evenements_crees = 0
        while evenements_crees < 60:
            # Choix aléatoire d'une discipline
            nom_disc, discipline = random.choice(list(disciplines.items()))
            epreuves_possibles = disciplines_data[nom_disc]

            # Choisir 1 à 3 épreuves uniques pour cet événement
            nb_epreuves = random.randint(1, min(3, len(epreuves_possibles)))
            epreuves_selectionnees = random.sample(epreuves_possibles, nb_epreuves)

            # Créer l'événement
            lieu = random.choice(lieux)
            evenement = Evenement.objects.create(
                description=f"{nom_disc} - Événement {evenements_crees + 1}",
                date=self.date_aleatoire(),
                horraire=self.heure_aleatoire(),
                lieu=lieu
            )

            # Créer les épreuves tout en respectant la contrainte unique
            epreuves_utilisees = set()
            for ep in epreuves_selectionnees:
                key = (ep["libelle"], ep["genre"], ep["tour"])
                if key in epreuves_utilisees:
                    continue  # éviter les doublons dans le même événement
                Epreuve.objects.create(
                    libelle=ep["libelle"],
                    genre=ep["genre"],
                    tour=ep["tour"],
                    discipline=discipline,
                    evenement=evenement
                )
                epreuves_utilisees.add(key)

            evenements_crees += 1

        self.stdout.write(self.style.SUCCESS("Base peuplée avec 60 événements JO et 1 à 3 épreuves chacun !"))
