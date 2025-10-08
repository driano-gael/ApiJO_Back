from django.test import TestCase
from users.models.base_user import User
from users.models.client import ClientProfile
from users.serializers.client import ClientSerializer, ClientFullSerializer


class ClientModelSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='client@example.com', password='P@ssword123456789', role='client')

    def test_client_model_generates_encrypted_key(self):
        client = ClientProfile.objects.create(user=self.user, nom='Durand', prenom='Alice', telephone='0601020304')
        self.assertIsNotNone(client.cle_chiffree)
        self.assertEqual(len(client.cle_chiffree), 64)  # SHA256

    def test_client_serializer_output(self):
        client = ClientProfile.objects.create(user=self.user, nom='Durand', prenom='Alice', telephone='0601020304')
        serializer = ClientFullSerializer(instance=client)
        self.assertEqual(serializer.data['nom'], 'Durand')
        self.assertIn('cle_chiffree', serializer.data)
        self.assertEqual(serializer.data['cle_chiffree'], client.cle_chiffree)

    def test_client_create_is_a_client(self):
        client = ClientProfile.objects.create(user=self.user, nom='Durand', prenom='Alice', telephone='0601020304')
        self.assertEqual(client.user.role, 'client')
