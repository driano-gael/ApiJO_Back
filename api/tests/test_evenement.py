from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from api.models import Evenement, Lieu
from users.models.base_user import User
from datetime import date, time
from api.serializers import EvenementSerializer

# ---------- MODELE ----------
class EvenementModelTest(TestCase):
    def test_str_representation(self):
        lieu = Lieu.objects.create(nom="Stade Pierre Mauroy")
        evenement = Evenement.objects.create(
            description="100m Final",
            lieu=lieu,
            date=date(2025, 8, 1),
            horraire=time(15, 0)
        )
        self.assertEqual(str(evenement), "100m Final")

# ---------- SERIALIZER ----------
class EvenementSerializerTest(TestCase):
    def test_serializer_content(self):
        lieu = Lieu.objects.create(nom="Bercy")
        evenement = Evenement.objects.create(
            description="Boxe - Quart de finale",
            lieu=lieu,
            date=date(2025, 7, 30),
            horraire=time(18, 30)
        )
        serializer = EvenementSerializer(instance=evenement)
        self.assertEqual(serializer.data['id'], evenement.id)
        self.assertEqual(serializer.data['lieu']['id'], lieu.id)
        self.assertEqual(serializer.data['date'], str(evenement.date))
        self.assertEqual(serializer.data['horraire'], evenement.horraire.strftime("%H:%M:%S"))

# ---------- API ----------
class EvenementAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.lieu = Lieu.objects.create(nom="Grand Palais")
        self.evenement = Evenement.objects.create(
            description="Escrime - Demi-finale",
            lieu=self.lieu,
            date=date(2025, 8, 5),
            horraire=time(11, 0)
        )

        self.admin_user = User.objects.create_admin(
            email="admin@example.com",
            password="Adminp@ss123456789"
        )
        self.super_user = User.objects.create_superuser(
            email="super@example.com",
            password="Superp@ss123456789"
        )
        self.normal_user = User.objects.create_user(
            email="user@example.com",
            password="Userp@ss123456789"
        )

    def test_get_list_evenements(self):
        response = self.client.get(reverse('evenement-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Escrime - Demi-finale", str(response.data))

    def test_get_detail_evenement(self):
        response = self.client.get(reverse('evenement-detail', kwargs={'pk': self.evenement.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], self.evenement.description)

    def test_create_evenement_unauthenticated_fail(self):
        response = self.client.post(reverse('evenement-create'), data={
            'description': 'Nouveau match',
            'lieu_id': self.lieu.id,
            'date': '2025-08-10',
            'horraire': '16:00:00'
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_evenement_user_fail(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.post(reverse('evenement-create'), data={
            'description': 'Interdit',
            'lieu_id': self.lieu.id,
            'date': '2025-08-12',
            'horraire': '19:00:00'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_evenement_admin_succeed(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.post(reverse('evenement-create'), data={
            'description': 'Finale Natation',
            'lieu_id': self.lieu.id,
            'date': '2025-08-15',
            'horraire': '10:00:00'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Evenement.objects.filter(description="Finale Natation").exists())

    def test_update_evenement_unauthenticated_fail(self):
        url = reverse('evenement-update', kwargs={'pk': self.evenement.id})
        response = self.client.put(url, data={
            'description': 'Modifié',
            'lieu_id': self.lieu.id,
            'date': '2025-08-05',
            'horraire': '11:00:00'
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_evenement_user_fail(self):
        self.client.force_authenticate(user=self.normal_user)
        url = reverse('evenement-update', kwargs={'pk': self.evenement.id})
        response = self.client.put(url, data={
            'description': 'Tentative Modif',
            'lieu_id': self.lieu.id,
            'date': '2025-08-05',
            'horraire': '11:00:00'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_evenement_admin_succeed(self):
        self.client.force_authenticate(user=self.admin_user)
        url = reverse('evenement-update', kwargs={'pk': self.evenement.id})
        response = self.client.put(url, data={
            'description': 'Modifié par admin',
            'lieu_id': self.lieu.id,
            'date': '2025-08-05',
            'horraire': '11:00:00'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.evenement.refresh_from_db()
        self.assertEqual(self.evenement.description, 'Modifié par admin')

    def test_delete_evenement_unauthenticated_fail(self):
        url = reverse('evenement-delete', kwargs={'pk': self.evenement.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertTrue(Evenement.objects.filter(pk=self.evenement.id).exists())

    def test_delete_evenement_user_fail(self):
        self.client.force_authenticate(user=self.normal_user)
        url = reverse('evenement-delete', kwargs={'pk': self.evenement.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Evenement.objects.filter(pk=self.evenement.id).exists())

    def test_delete_evenement_admin_succeed(self):
        self.client.force_authenticate(user=self.admin_user)
        url = reverse('evenement-delete', kwargs={'pk': self.evenement.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Evenement.objects.filter(pk=self.evenement.id).exists())
