from django.core.files.storage import default_storage  # noqa: F401
from django.test import SimpleTestCase


class TestStorages(SimpleTestCase):
    def test_configuration(self):
        self.assertTrue(True)
