from django.contrib.auth import get_user_model
from django.test import TestCase

from project.users.serializers import UserSerializer


class TestRegistrationView(TestCase):
    def setUp(self):
        self.data = {"username": "jeff", "email": "jeffs@mail.com", "password": "password"}
        self.existing = {
            "username": "existing",
            "email": "existing@mail.com",
            "password": "password",
        }
        self.user_manager = get_user_model().objects
        self.user_manager.create_user(**self.existing)

    def test_user_creation(self):
        serializer = UserSerializer(data=self.data)

        if serializer.is_valid():
            user = serializer.save()
        else:
            self.fail(serializer.errors)

        self.assertEqual(user, self.user_manager.get(username=self.data["username"]))

    def test_missing_data_user_validation(self):
        serializer = UserSerializer(data={})
        serializer.is_valid()
        self.assertEqual(len(serializer.errors), 3)

    def test_existing_user_validation(self):
        serializer = UserSerializer(data=self.existing)
        serializer.is_valid()
        self.assertEqual(len(serializer.errors), 2)

    def test_serialization(self):
        user = self.user_manager.get(username=self.existing["username"])
        serializer = UserSerializer(user)
        self.assertDictEqual(
            serializer.data, {k: v for k, v in self.existing.items() if k != "password"}
        )
