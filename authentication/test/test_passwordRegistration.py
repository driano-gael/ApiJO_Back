from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.response import Response
from typing import cast

class ClientPasswordValidationTests(APITestCase):
    def setUp(self):
        self.url = reverse('register-client')
        self.base_data = {
            'email': 'client@example.com',
            'nom': 'Durand',
            'prenom': 'Alice',
            'telephone': '0601020304',
        }

    def _post_with_password(self, password: str) -> Response:
        data = self.base_data.copy()
        data['password'] = password
        return cast(Response, self.client.post(self.url, data, format='json'))

    def test_password_too_short(self):
        response = self._post_with_password('abc123')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)
        self.assertIn('too short', str(response.data['password']).lower())

    def test_password_common(self):
        response = self._post_with_password('password')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)
        self.assertIn('too common', str(response.data['password']).lower())

    def test_password_numeric_only(self):
        response = self._post_with_password('12345678')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)
        self.assertIn('entirely numeric', str(response.data['password']).lower())

    def test_password_similar_to_email(self):
        response = self._post_with_password('client@example.com')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)
        self.assertIn('too similar', str(response.data['password']).lower())

    def test_password_valid(self):
        response = self._post_with_password('Secur3P@ssw0rd!')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)