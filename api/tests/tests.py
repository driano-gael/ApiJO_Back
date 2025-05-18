from django.test import TestCase

class BasicMathTest(TestCase):
    def test_primaire(self):
        self.assertEqual(1+1, 2)