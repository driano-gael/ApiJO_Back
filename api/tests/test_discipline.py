from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Discipline
from users.models.base_user import User
from django.urls import reverse
from api.serializers import DisciplineSerializer


# ---------- MODELE ----------
class DisciplineModelTest(TestCase):
    def test_str_representation(self):
        discipline = Discipline.objects.create(nom="Boxe")
        self.assertEqual(str(discipline), "Boxe")

# ---------- SERIALIZER ----------

class DisciplineSerializerTest(TestCase):
    def test_serializer_content(self):
        discipline = Discipline.objects.create(nom="tennis", icone="aaa")
        serializer = DisciplineSerializer(instance=discipline)
        self.assertEqual(serializer.data, {'id': discipline.id, 'nom': "tennis", 'icone': "aaa"})

# ---------- API ----------
class DisciplineAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.discipline = Discipline.objects.create(nom="Boxe")

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

    def test_get_list_lieux(self):
        response = self.client.get(reverse('discipline-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Boxe", str(response.data))

    def test_get_detail_lieu(self):
        response = self.client.get(reverse('discipline-detail', kwargs={'pk': self.discipline.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nom'], self.discipline.nom)

    def test_create_lieu_unauthenticated_fail(self):
        response = self.client.post(reverse('discipline-create'), data={'nom': 'Nouveau Discipline'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_lieu_user_fail(self):
        self.client.login(email="user@example.com", password="Userp@ss123456789")
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.post(reverse('discipline-create'), data={'nom': 'Discipline Interdit'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_lieu_admin_succed(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.post(reverse('discipline-create'), data={'nom': 'Discipline Admin'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Discipline.objects.filter(nom='Discipline Admin').exists())

    def test_update_lieu_unauthenticated_fail(self):
        url = reverse('discipline-update', kwargs={'pk': self.discipline.id})
        response = self.client.put(url, data={'nom': 'Lieu Modifié'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.discipline.refresh_from_db()
        self.assertEqual(self.discipline.nom, 'Boxe')

    def test_update_lieu_user_fail(self):
        self.client.login(email="user@example.com", password="Userp@ss123456789")
        self.client.force_authenticate(user=self.normal_user)
        url = reverse('discipline-update', kwargs={'pk': self.discipline.id})
        response = self.client.put(url, data={'nom': 'Discipline Modifié'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.discipline.refresh_from_db()
        self.assertEqual(self.discipline.nom, 'Boxe')

    def test_update_lieu_admin_succed(self):
        self.client.force_authenticate(user=self.admin_user)
        url = reverse('discipline-update', kwargs={'pk': self.discipline.id})
        response = self.client.put(url, data={'nom': 'Discipline Modifié'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.discipline.refresh_from_db()
        self.assertEqual(self.discipline.nom, 'Discipline Modifié')

    def test_delete_lieu_unauthenticated_fail(self):
        url = reverse('discipline-delete', kwargs={'pk': self.discipline.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertTrue(Discipline.objects.filter(pk=self.discipline.id).exists())

    def test_delete_lieu_user_fail(self):
        self.client.login(email="user@example.com", password="Userp@ss123456789")
        self.client.force_authenticate(user=self.normal_user)
        url = reverse('discipline-delete', kwargs={'pk': self.discipline.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Discipline.objects.filter(pk=self.discipline.id).exists())

    def test_delete_lieu_admin_succed(self):
        self.client.force_authenticate(user=self.admin_user)
        url = reverse('discipline-delete', kwargs={'pk': self.discipline.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Discipline.objects.filter(pk=self.discipline.id).exists())

    def test_create_discipline_invalid_data(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.post(reverse('discipline-create'), data={})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('nom', response.data)

    def test_serializer_invalid(self):
        serializer = DisciplineSerializer(data={})
        self.assertFalse(serializer.is_valid())
        self.assertIn('nom', serializer.errors)
