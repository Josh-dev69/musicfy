from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.

class UserAuthenticationTest(TestCase):
    def test_unique_username(self):
        response = self.client.post(reverse('register'), {'username': 'testuser', 'email': 'test@example.com', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Check if user is redirected after registration
        self.assertTrue(User.objects.filter(username='testuser').exists())  # Check if user is created successfully

    def test_valid_credentials(self):
        User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Check if user is redirected after login
