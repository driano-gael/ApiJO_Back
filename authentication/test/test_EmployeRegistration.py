from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models.base_user import User
from rest_framework.response import Response
from typing import cast
from rest_framework.test import APIClient

class EmployeeRegistrationTests(APITestCase):

    def setUp(self):
        self.client: APIClient
        self.url = reverse('register-employe')
        self.valid_data = {
            'email': 'employe@example.com',
            'password': 'Password123!',
            'nom': 'Smith',
            'prenom': 'John',
            'matricule': 'EMP001',
            'identifiant_telephone': '1234567890'
        }

        self.admin_user = User.objects.create_user(
            email='admin@example.com',
            password='AdminPassword123!',
            role='admin',
            is_staff=True
        )
        self.client.force_authenticate(user=self.admin_user)

    def test_register_employee_success(self):
        response = self.client.post(self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email='employe@example.com').exists())
        user = User.objects.get(email='employe@example.com')
        self.assertEqual(user.role, 'employe')
        self.assertTrue(hasattr(user, 'employe_profile'))
        self.assertEqual(user.employe_profile.matricule, 'EMP001')

    def test_register_employee_missing_fields(self):
        incomplete_data = self.valid_data.copy()
        incomplete_data.pop('matricule')
        response = cast(Response, self.client.post(self.url, incomplete_data, format='json'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('matricule', response.data)

    def test_register_employee_duplicate_email(self):
        User.objects.create_user(email='employe@example.com', password='dummy', role='employe')
        response = cast(Response, self.client.post(self.url, self.valid_data, format='json'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    def test_register_employee_invalid_email(self):
        invalid_data = self.valid_data.copy()
        invalid_data['email'] = 'not-an-email'
        response = cast(Response, self.client.post(self.url, invalid_data, format='json'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    def test_register_employee_short_password(self):
        invalid_data = self.valid_data.copy()
        invalid_data['password'] = '123'
        response = cast(Response, self.client.post(self.url, invalid_data, format='json'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)