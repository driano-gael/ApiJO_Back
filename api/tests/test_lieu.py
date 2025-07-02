from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Lieu
from users.models.base_user import User
from django.urls import reverse

# ---------- MODELE ----------
class LieuModelTest(TestCase):
    def test_str_representation(self):
        lieu = Lieu.objects.create(nom="Stade de France")
        self.assertEqual(str(lieu), "Stade de France")

# ---------- SERIALIZER ----------
from api.serializers import LieuSerializer

class LieuSerializerTest(TestCase):
    def test_serializer_content(self):
        lieu = Lieu.objects.create(nom="Roland-Garros")
        serializer = LieuSerializer(instance=lieu)
        self.assertEqual(serializer.data, {'id': lieu.id, 'nom': "Roland-Garros"})

# ---------- API ----------
class LieuAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.lieu = Lieu.objects.create(nom="Accor Arena")

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
        response = self.client.get(reverse('lieu-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Accor Arena", str(response.data))

    def test_get_detail_lieu(self):
        response = self.client.get(reverse('lieu-detail', kwargs={'pk': self.lieu.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nom'], self.lieu.nom)

    def test_create_lieu_unauthenticated_fail(self):
        response = self.client.post(reverse('lieu-create'), data={'nom': 'Nouveau Lieu'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_lieu_user_fail(self):
        self.client.login(email="user@example.com", password="Userp@ss123456789")
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.post(reverse('lieu-create'), data={'nom': 'Lieu Interdit'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_lieu_admin_succed(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.post(reverse('lieu-create'), data={'nom': 'Lieu Admin'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Lieu.objects.filter(nom='Lieu Admin').exists())

    def test_update_lieu_unauthenticated_fail(self):
        url = reverse('lieu-update', kwargs={'pk': self.lieu.id})
        response = self.client.put(url, data={'nom': 'Lieu Modifié'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.lieu.refresh_from_db()
        self.assertEqual(self.lieu.nom, 'Accor Arena')

    def test_update_lieu_user_fail(self):
        self.client.login(email="user@example.com", password="Userp@ss123456789")
        self.client.force_authenticate(user=self.normal_user)
        url = reverse('lieu-update', kwargs={'pk': self.lieu.id})
        response = self.client.put(url, data={'nom': 'Lieu Modifié'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.lieu.refresh_from_db()
        self.assertEqual(self.lieu.nom, 'Accor Arena')

    def test_update_lieu_admin_succed(self):
        self.client.force_authenticate(user=self.admin_user)
        url = reverse('lieu-update', kwargs={'pk': self.lieu.id})
        response = self.client.put(url, data={'nom': 'Lieu Modifié'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.lieu.refresh_from_db()
        self.assertEqual(self.lieu.nom, 'Lieu Modifié')

    def test_delete_lieu_unauthenticated_fail(self):
        url = reverse('lieu-delete', kwargs={'pk': self.lieu.id})
        response = self.client.put(url, data={'nom': 'Lieu Modifié'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        response = self.client.delete(url)
        self.assertTrue(Lieu.objects.filter(pk=self.lieu.id).exists())

    def test_delete_lieu_user_fail(self):
        self.client.login(email="user@example.com", password="Userp@ss123456789")
        self.client.force_authenticate(user=self.normal_user)
        url = reverse('lieu-delete', kwargs={'pk': self.lieu.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Lieu.objects.filter(pk=self.lieu.id).exists())

    def test_delete_lieu_admin_succed(self):
        self.client.force_authenticate(user=self.admin_user)
        url = reverse('lieu-delete', kwargs={'pk': self.lieu.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lieu.objects.filter(pk=self.lieu.id).exists())
