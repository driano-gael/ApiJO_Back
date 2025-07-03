from django.test import TestCase
from users.models.base_user import User
from users.models.admin import AdminProfile
from users.serializers.admin import AdminSerializer

class AdminModelSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='admin@example.com', password='@dminpAss123456789', role='admin')

    def test_admin_model(self):
        admin = AdminProfile.objects.create(
            user=self.user,
            nom='Legrand',
            prenom='Sophie',
            matricule='ADM999'
        )
        self.assertEqual(admin.nom, 'Legrand')
        self.assertEqual(admin.user.email, 'admin@example.com')

    def test_admin_serializer(self):
        admin = AdminProfile.objects.create(
            user=self.user,
            nom='Legrand',
            prenom='Sophie',
            matricule='ADM999'
        )
        serializer = AdminSerializer(instance=admin)
        self.assertEqual(serializer.data['matricule'], 'ADM999')

    def test_admin_created_is_an_admin(self):
        admin = AdminProfile.objects.create(
            user=self.user,
            nom='Legrand',
            prenom='Sophie',
            matricule='ADM999'
        )
        self.assertEqual(admin.user.role, 'admin')