from unittest import TestCase
import uuid
from django.contrib.auth import get_user_model


class UserModelTestCase(TestCase):
    def setUp(self):
        self.User = get_user_model()

    def test_create_user(self):
        """Test creating a new user"""
        email = f'test_{uuid.uuid4()}@example.com'
        user = self.User.objects.create_user(
            email=email,
            password='testpassword'
        )
        self.assertIsNotNone(user)  # Check that user is not None
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password('testpassword'))
        self.assertTrue(user.is_active)

    def test_delete_user(self):
        """Test deleting a user"""
        email = f'delete_{uuid.uuid4()}@example.com'
        user = self.User.objects.create_user(
            email=email,
            password='testpassword'
        )
        user.delete()
        deleted_user = self.User.objects.filter(email=email, is_delete=True).first()
        self.assertIsNotNone(deleted_user)

