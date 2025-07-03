from django.test import TestCase
from users.models.base_user import User
from users.models.employe import EmployeProfile
from users.serializers.employe import EmployeSerializer

class EmployeModelSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='employe@example.com', password='securepass', role='employe')

    def test_employe_model_creation(self):
        employe = EmployeProfile.objects.create(
            user=self.user,
            nom='Martin',
            prenom='Clara',
            matricule='EMP123',
            identifiant_telephone='IDT987'
        )
        self.assertEqual(employe.nom, 'Martin')
        self.assertEqual(employe.identifiant_telephone, 'IDT987')

    def test_employe_serializer_output(self):
        employe = EmployeProfile.objects.create(
            user=self.user,
            nom='Martin',
            prenom='Clara',
            matricule='EMP123',
            identifiant_telephone='IDT987'
        )
        serializer = EmployeSerializer(instance=employe)
        self.assertEqual(serializer.data['matricule'], 'EMP123')

    def test_employe_create_is_an_employe(self):
        employe = EmployeProfile.objects.create(
            user=self.user,
            nom='Martin',
            prenom='Clara',
            matricule='EMP123',
            identifiant_telephone='IDT987'
        )
        self.assertEqual(employe.user.role, 'employe')