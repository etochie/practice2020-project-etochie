from rest_framework.test import APITestCase
from django.urls import reverse


class AuthTokenTests(APITestCase):
    def setUp(self):
        new_user_data = {
            'username': 'test_username',
            'password': 'test_password123'
        }

        self.new_user_data = new_user_data

    def test_register_token_response(self):
        url = reverse('users-list')
        response = self.client.post(url, self.new_user_data)

        self.assertTrue('token' in response.data)

    def test_obtain_auth_token_response(self):
        self.client.post(reverse('users-list'), self.new_user_data)
        url = reverse('auth-token-create')
        response = self.client.post(url, data=self.new_user_data)

        self.assertTrue('token' in response.data)
