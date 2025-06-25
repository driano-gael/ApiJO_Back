from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models.base_user import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIClient


def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)

class EmployeePermissionTests(APITestCase):
    def setUp(self):
        self.client: APIClient = APIClient()
        self.url = reverse("register-employe")

        # Admin
        self.admin_user = User.objects.create_user(
            email="admin@example.com",
            password="adminpass123",
            role="admin",
            is_staff=True
        )

        # Client
        self.client_user = User.objects.create_user(
            email="client@example.com",
            password="clientpass123",
            role="client"
        )

        # Employé
        self.employee_user = User.objects.create_user(
            email="employee@example.com",
            password="employeepass123",
            role="employe"
        )

    def test_admin_can_access_employee_register(self):
        token = get_token_for_user(self.admin_user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        data = {
            "email": "newemp@example.com",
            "password": "StrongPass123",
            "nom": "Test",
            "prenom": "User",
            "matricule": "EMP999",
            "identifiant_telephone": "0102030405"
        }

        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_client_cannot_access_employee_register(self):
        token = get_token_for_user(self.client_user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        response = self.client.post(self.url, {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_employee_cannot_access_employee_register(self):
        token = get_token_for_user(self.employee_user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        response = self.client.post(self.url, {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthenticated_user_cannot_access_employee_register(self):
        response = self.client.post(self.url, {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)