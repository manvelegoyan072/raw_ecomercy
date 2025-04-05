from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class RegisterTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_user(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword',
            'first_name': 'Test',
            'last_name': 'User'
        }
        response = self.client.post('/raw_api/auth/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('user', response.data)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)