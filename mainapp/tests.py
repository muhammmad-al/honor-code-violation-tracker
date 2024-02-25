from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site


class LoginFlowTestCase(TestCase):

    def setUp(self):
        # Create a test user and superuser for authentication
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='12345')
        self.admin_user = User.objects.create_superuser(username='adminuser', email='admin@example.com',
                                                        password='admin123')

        # Setup for django-allauth SocialApp
        site = Site.objects.get_current()
        social_app = SocialApp.objects.create(
            provider='google',
            name='Google',
            client_id='test_client_id',
            secret='test_secret_key',
        )
        social_app.sites.add(site)

    def test_index_page(self):
        # Test that the index page loads correctly
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to My Google OAuth Project")

    def test_user_login_page(self):
        # Test that the user login page loads correctly
        response = self.client.get(reverse('user_login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Login With Google")

    def test_admin_login_page(self):
        # Test that the admin login page loads correctly
        response = self.client.get(reverse('admin_login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Login With Google")

    def test_logout_accessible(self):
        # Test that the logout URL is accessible
        response = self.client.get('/logout')
        # Depending on your LOGOUT_REDIRECT_URL setting, this might redirect, hence checking for 302
        self.assertEqual(response.status_code, 302)
