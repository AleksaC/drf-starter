from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model
from django.urls import reverse


class TestRegistrationView(APITestCase):
    def setUp(self):
        self.url = reverse("users:register")
        self.existing = {
            "username": "existing",
            "email": "existing@mail.com",
            "password": "irrelevant",
        }
        get_user_model().objects.create_user(**self.existing)

    def test_successful_registration(self):
        data = {"username": "name", "email": "test@mail.com", "password": "mypassword"}
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_missing_data_failing_registration(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(len(response.json()), 3)

    def test_existing_username_and_email_failing_registration(self):
        response = self.client.post(self.url, data=self.existing)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(len(response.json()), 2)
