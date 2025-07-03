from django.test import TestCase
from users.models.base_user import User

class UserModelTest(TestCase):
    def test_create_user_with_valid_data(self):
        user = User.objects.create_user(email='test@example.com', password='Securep@ss123456789', role='client')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('Securep@ss123456789'))
        self.assertEqual(user.role, 'client')