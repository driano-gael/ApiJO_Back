from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models.base_user import User
from rest_framework.response import Response
from typing import cast

class ClientRegistrationTests(APITestCase):
    def setUp(self):
        self.url = reverse('register-client')
        self.valid_data = {
            'email': 'client@example.com',
            'password': 'Strongpassword123#',
            'nom': 'Dupont',
            'prenom': 'Jean',
            'telephone': '0601020304'
        }

    def test_register_client_success(self):
        response = cast(Response, self.client.post(self.url, self.valid_data, format='json'))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email=self.valid_data['email']).exists())

    def test_register_client_missing_fields(self):
        incomplete_data = self.valid_data.copy()
        incomplete_data.pop('nom')  # Suppression d’un champ obligatoire
        response = cast(Response, self.client.post(self.url, incomplete_data, format='json'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('nom', response.data)

    def test_register_client_missing_email(self):
        incomplete_data = self.valid_data.copy()
        incomplete_data.pop('email')
        response = cast(Response, self.client.post(self.url, incomplete_data, format='json'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    def test_register_client_duplicate_email(self):
        User.objects.create_user(email=self.valid_data['email'], password='dummy', role='client')
        response = cast(Response, self.client.post(self.url, self.valid_data, format='json'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)