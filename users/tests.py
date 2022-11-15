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
        # print(response.data)
        self.assertEqual(response.data, {'message': '가입 완료!!'})

