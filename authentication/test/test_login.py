from rest_framework.test import APITestCase
from django.urls import reverse
from users.models.base_user import User
from rest_framework import status
from rest_framework.response import Response
from typing import cast

class LoginTests(APITestCase):
    def setUp(self):
        # Création des utilisateurs avec différents rôles
        self.admin = User.objects.create_user(email='admin@example.com', password='adminpass123', role='admin', is_staff=True)
        self.employe = User.objects.create_user(email='employe@example.com', password='employeepass123', role='employe')
        self.client_user = User.objects.create_user(email='client@example.com', password='clientpass123', role='client')

        self.url = reverse('login')

    def test_admin_login_success(self):
        data = {'email': 'admin@example.com', 'password': 'adminpass123'}
        response = cast(Response, self.client.post(self.url, data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertEqual(response.data['role'], 'admin')

    def test_employe_login_success(self):
        data = {'email': 'employe@example.com', 'password': 'employeepass123'}
        response = cast(Response, self.client.post(self.url, data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertEqual(response.data['role'], 'employe')

    def test_client_login_success(self):
        data = {'email': 'client@example.com', 'password': 'clientpass123'}
        response = cast(Response, self.client.post(self.url, data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertEqual(response.data['role'], 'client')

    def test_login_failure_wrong_password(self):
        data = {'email': 'admin@example.com', 'password': 'wrongpassword'}
        response = cast(Response, self.client.post(self.url, data))
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_400_BAD_REQUEST])

    def test_login_failure_nonexistent_user(self):
        data = {'email': 'nouser@example.com', 'password': 'somepassword'}
        response = cast(Response, self.client.post(self.url, data))
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_400_BAD_REQUEST])
