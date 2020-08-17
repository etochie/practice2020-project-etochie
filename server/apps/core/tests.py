from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from apps.core.models import Cafe, Dish


class CafeAPITests(APITestCase):
    def setUp(self):
        owner = User.objects.create(username='test_owner', password='test_password')
        user = User.objects.create(username='test_user', password='test_password')
        owner_token = Token.objects.create(user=owner)
        user_token = Token.objects.create(user=user)

        Cafe.objects.create(
            name='test_cafe',
            open_hour=10,
            close_hour=2,
            address='Красноярск Мира 12',
            owner=User.objects.get(username='test_owner')
        )

        self.cafe_id = Cafe.objects.get(name='test_cafe').id
        self.owner_token = owner_token.key
        self.user_token = user_token.key
        self.data = {
            'name': 'test_cafe_edit',
            'open_hour': 10,
            'close_hour': 2,
            'address': 'Красноярск Мира 12',
        }

    def test_owner_cafe_put_action(self):
        url = reverse('cafe-detail', kwargs={'pk': self.cafe_id})
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.owner_token)
        response = self.client.put(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_owner_cafe_patch_action(self):
        url = reverse('cafe-detail', kwargs={'pk': self.cafe_id})
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.owner_token)
        response = self.client.patch(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_owner_cafe_delete_action(self):
        url = reverse('cafe-detail', kwargs={'pk': self.cafe_id})
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.owner_token)
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_authorized_cafe_put_action(self):
        url = reverse('cafe-detail', kwargs={'pk': self.cafe_id})
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token)
        response = self.client.put(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authorized_cafe_patch_action(self):
        url = reverse('cafe-detail', kwargs={'pk': self.cafe_id})
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token)
        response = self.client.patch(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authorized_cafe_delete_action(self):
        url = reverse('cafe-detail', kwargs={'pk': self.cafe_id})
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token)
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthorized_cafe_put_action(self):
        url = reverse('cafe-detail', kwargs={'pk': self.cafe_id})
        response = self.client.put(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthorized_cafe_patch_action(self):
        url = reverse('cafe-detail', kwargs={'pk': self.cafe_id})
        response = self.client.patch(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthorized_cafe_delete_action(self):
        url = reverse('cafe-detail', kwargs={'pk': self.cafe_id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthorized_cafe_get_action(self):
        url = reverse('cafe-detail', kwargs={'pk': self.cafe_id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthorized_cafe_list_action(self):
        url = reverse('cafe-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authorized_cafe_post_action(self):
        url = reverse('cafe-list')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token)
        response = self.client.post(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthorized_cafe_post_action(self):
        url = reverse('cafe-list')
        response = self.client.post(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class DishAPITests(APITestCase):
    def setUp(self):
        owner = User.objects.create(username='test_owner', password='test_password')
        user = User.objects.create(username='test_user', password='test_password')
        owner_token = Token.objects.create(user=owner)
        user_token = Token.objects.create(user=user)

        Cafe.objects.create(
            name='test_cafe',
            open_hour=10,
            close_hour=2,
            address='Красноярск Мира 12',
            owner=User.objects.get(username='test_owner')
        )
        Dish.objects.create(
            name='test_dish',
            price=100,
            cafe=Cafe.objects.get(name='test_cafe')
        )

        self.cafe_id = Cafe.objects.get(name='test_cafe').id
        self.dish_id = Dish.objects.get(name='test_dish').id
        self.owner_token = owner_token.key
        self.user_token = user_token.key
        self.data = {
            'name': 'test_dish_edit',
            'price': 200,
            'cafe': self.cafe_id
        }

    def test_owner_dish_put_action(self):
        url = reverse('dish-detail', kwargs={'pk': self.dish_id})
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.owner_token)
        response = self.client.put(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_owner_dish_patch_action(self):
        url = reverse('dish-detail', kwargs={'pk': self.dish_id})
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.owner_token)
        response = self.client.patch(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_owner_dish_delete_action(self):
        url = reverse('dish-detail', kwargs={'pk': self.dish_id})
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.owner_token)
        response = self.client.delete(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_authorized_dish_put_action(self):
        url = reverse('dish-detail', kwargs={'pk': self.dish_id})
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token)
        response = self.client.put(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authorized_dish_patch_action(self):
        url = reverse('dish-detail', kwargs={'pk': self.dish_id})
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token)
        response = self.client.patch(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authorized_dish_delete_action(self):
        url = reverse('dish-detail', kwargs={'pk': self.dish_id})
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token)
        response = self.client.delete(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthorized_dish_put_action(self):
        url = reverse('dish-detail', kwargs={'pk': self.dish_id})
        response = self.client.put(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthorized_dish_patch_action(self):
        url = reverse('dish-detail', kwargs={'pk': self.dish_id})
        response = self.client.patch(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthorized_dish_delete_action(self):
        url = reverse('dish-detail', kwargs={'pk': self.dish_id})
        response = self.client.delete(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthorized_dish_get_action(self):
        url = reverse('dish-detail', kwargs={'pk': self.dish_id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthorized_dish_list_action(self):
        url = reverse('dish-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_owner_dish_post_action(self):
        url = reverse('dish-list')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.owner_token)
        response = self.client.post(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_authorized_dish_post_action(self):
        url = reverse('dish-list')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token)
        response = self.client.post(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthorized_dish_post_action(self):
        url = reverse('dish-list')
        response = self.client.post(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
