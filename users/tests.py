from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User


class UserRegistrationTest(APITestCase):
    def test_registration(self):
        url = reverse("user_view")
        user_data = {
        "username" : "testuser",
        "password" : "password",
        "email" : "test@test.com",
        "fullname" : "테스터",
        }
        response = self.client.post(url, user_data)        
        self.assertEqual(response.status_code, 200)

