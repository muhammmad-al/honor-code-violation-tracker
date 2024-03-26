import os
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp
from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import HonorCodeViolation
from datetime import date
from django.urls import reverse
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from mainapp.forms import HonorCodeViolationForm

class HonorCodeViolationModelTests(TestCase):
    def test_model_str(self):
        violation = HonorCodeViolation(name="Test Name", date_of_incident=date.today(), description="Test Description")
        self.assertEqual(str(violation), f"Violation by Test Name on {date.today()}")

    def test_invalid_date(self):
        violation = HonorCodeViolation(date_of_incident="not a date", description="Test")
        with self.assertRaises(ValidationError):
            violation.full_clean()

class IndexViewTests(TestCase):
    def setUp(self):
        site = Site.objects.create(domain='test.com', name='test')
        app = SocialApp.objects.create(provider='google', name='Google', client_id='client_id', secret='secret', key='')
        app.sites.add(site)
        settings.SITE_ID = site.id

    def test_index_view_status_code(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    def test_admin_login_view_access_without_authentication(self):
        response = self.client.get(reverse('admin_dashboard_url'))
        self.assertEqual(response.status_code, 200)
class UserLoginAndFileUploadTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_login_screen(self):
        response = self.client.get(reverse('user_dashboard_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_dashboard.html')

    def test_upload_txt_file(self):
        test_file_path = os.path.join(settings.BASE_DIR, 'mainapp', 'test_files', 'test.txt')

        with open(test_file_path, 'rb') as file:
            response = self.client.post(reverse('user_dashboard_url'), {
                'name': 'Test Name',
                'date_of_incident': '2024-03-01',
                'description': 'Test Description',
                'file': SimpleUploadedFile(file.name, file.read(), content_type='text/plain'),
            })
            self.assertEqual(response.status_code, 302)

    def test_upload_pdf_file(self):
        test_file_path = os.path.join(settings.BASE_DIR, 'mainapp', 'test_files', 'test.pdf')

        with open(test_file_path, 'rb') as file:
            response = self.client.post(reverse('user_dashboard_url'), {
                'name': 'Test Name',
                'date_of_incident': '2024-03-01',
                'description': 'Test Description',
                'file': SimpleUploadedFile(file.name, file.read(), content_type='application/pdf'),
            })
            self.assertEqual(response.status_code, 302)

    def test_upload_jpg_file(self):
        test_file_path = os.path.join(settings.BASE_DIR, 'mainapp', 'test_files', 'test.jpg')

        with open(test_file_path, 'rb') as file:
            response = self.client.post(reverse('user_dashboard_url'), {
                'name': 'Test Name',
                'date_of_incident': '2024-03-01',
                'description': 'Test Description',
                'file': SimpleUploadedFile(file.name, file.read(), content_type='image/jpeg'),
            })
            self.assertEqual(response.status_code, 302)
