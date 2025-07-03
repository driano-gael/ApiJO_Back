from datetime import date, time

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from api.models import Epreuve, Discipline, Evenement, Lieu
from api.serializers import EpreuveSerializer
from users.models.base_user import User

# ---------- MODELE ----------
class EpreuveModelTest(TestCase):
    def test_str_representation(self):
        lieu = Lieu.objects.create(nom="Stade de France")
        discipline = Discipline.objects.create(nom="Athlétisme")
        evenement = Evenement.objects.create(description="JO 2024",
                                             lieu=lieu,
                                             date=date(2025, 8, 1),
                                             horraire=time(14, 0)
                                             )
        epreuve = Epreuve.objects.create(libelle="100m", discipline=discipline, evenement=evenement)
        self.assertEqual(str(epreuve), "100m")

# ---------- SERIALIZER ----------
class EpreuveSerializerTest(TestCase):
    def test_serializer_content(self):
        lieu = Lieu.objects.create(nom="Stade de France")
        discipline = Discipline.objects.create(nom="Natation")
        evenement = Evenement.objects.create(
            description="JO 2024",
            lieu=lieu,
            date=date(2025, 8, 1),
            horraire=time(14, 0)
        )
        epreuve = Epreuve.objects.create(
            libelle="100m nage libre",
            discipline=discipline,
            evenement=evenement
        )
        serializer = EpreuveSerializer(instance=epreuve)
        self.assertEqual(serializer.data['libelle'], "100m nage libre")
        self.assertEqual(serializer.data['discipline']['id'], discipline.id)
        self.assertEqual(serializer.data['evenement']['id'], evenement.id)

# ---------- API ----------
class EpreuveAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.lieu = Lieu.objects.create(nom="Bercy Arena")
        self.discipline = Discipline.objects.create(nom="Boxe")
        self.evenement = Evenement.objects.create(description="JO 2024",
                                             lieu=self.lieu,
                                             date=date(2025, 8, 1),
                                             horraire=time(14, 0)
                                             )
        self.epreuve = Epreuve.objects.create(libelle="Poids lourd", discipline=self.discipline, evenement=self.evenement)

        self.admin_user = User.objects.create_admin(
            email="admin@example.com",
            password="Adminp@ss123456789",
        )
        self.super_user = User.objects.create_superuser(
            email="super@example.com",
            password="Superp@ss123456789",
        )
        self.normal_user = User.objects.create_user(
            email="user@example.com",
            password="Userp@ss123456789",
        )

    def test_get_list_epreuves(self):
        response = self.client.get(reverse('epreuve-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Poids lourd", str(response.data))

    def test_get_detail_epreuve(self):
        response = self.client.get(reverse('epreuve-detail', kwargs={'pk': self.epreuve.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['libelle'], self.epreuve.libelle)

    def test_create_epreuve_unauthenticated_fail(self):
        response = self.client.post(reverse('epreuve-create'), data={
            'libelle': 'Nouvelle Epreuve',
            'discipline': self.discipline.id,
            'evenement': self.evenement.id
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_epreuve_user_fail(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.post(reverse('epreuve-create'), data={
            'libelle': 'Interdit',
            'discipline': self.discipline.id,
            'evenement': self.evenement.id
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_epreuve_admin_succeed(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.post(reverse('epreuve-create'), data={
            'libelle': 'Combat Final',
            'discipline_id': self.discipline.id,
            'evenement_id': self.evenement.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Epreuve.objects.filter(libelle='Combat Final').exists())

    def test_update_epreuve_admin_succeed(self):
        self.client.force_authenticate(user=self.admin_user)
        url = reverse('epreuve-update', kwargs={'pk': self.epreuve.id})
        response = self.client.put(url, data={
            'libelle': 'Poids super lourd',
            'discipline_id': self.discipline.id,
            'evenement_id': self.evenement.id
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.epreuve.refresh_from_db()
        self.assertEqual(self.epreuve.libelle, 'Poids super lourd')

    def test_update_epreuve_user_fail(self):
        self.client.force_authenticate(user=self.normal_user)
        url = reverse('epreuve-update', kwargs={'pk': self.epreuve.id})
        response = self.client.put(url, data={
            'libelle': 'Modification non autorisée',
            'discipline_id': self.discipline.id,
            'evenement_id': self.evenement.id
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.epreuve.refresh_from_db()
        self.assertEqual(self.epreuve.libelle, 'Poids lourd')

    def test_delete_epreuve_admin_succeed(self):
        self.client.force_authenticate(user=self.admin_user)
        url = reverse('epreuve-delete', kwargs={'pk': self.epreuve.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Epreuve.objects.filter(pk=self.epreuve.id).exists())

    def test_delete_epreuve_user_fail(self):
        self.client.force_authenticate(user=self.normal_user)
        url = reverse('epreuve-delete', kwargs={'pk': self.epreuve.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Epreuve.objects.filter(pk=self.epreuve.id).exists())
