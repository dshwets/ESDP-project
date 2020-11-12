from io import BytesIO
from django.contrib.auth.models import Permission
from django.core.files.images import ImageFile
from PIL import Image
from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponseRedirect
from accounts.factories import UserFactory
from hostelguests.factories import GuestFactory
from hostelguests.models import Guest


class GuestCreateTestCase(TestCase):
    def setUp(self) -> None:
        self.guest = GuestFactory()
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_add_guest')

    def tearDown(self) -> None:
        self.client.logout()

    def test_unauthorized_get_create_guest(self):
        response = self.client.get(reverse('hostelguests:guest_create'))
        redirect_url = reverse('accounts:login') + '?next=' + reverse('hostelguests:guest_create')
        self.assertRedirects(response, redirect_url, status_code=302)

    def test_unauthorized_post_create_guest(self):
        response = self.client.post(reverse('hostelguests:guest_create'))
        redirect_url = reverse('accounts:login') + '?next=' + reverse('hostelguests:guest_create')
        self.check_redirect(response, redirect_url)

    def check_redirect(self, response, redirect_url):
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        self.assertEqual(response.url, redirect_url)

    def test_authorized_without_permission_get_create_guest(self):
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(reverse('hostelguests:guest_create'))
        self.assertEqual(response.status_code, 403)

    def create_test_image(self):
        file = BytesIO()
        image = Image.new('RGBA', size=(50, 50), color=(155, 0, 0))
        image.save(file, format='PNG')
        file.name = 'test.png'
        file.seek(0)
        print(file)
        return ImageFile(file)


    def test_authorized_without_permission_post_create_add(self):
        url = reverse('hostelguests:guest_create')
        data = {
            'first_name': 'Testname',
            'last_name': 'Test',
            'middle_name': 'TestMiddle',
            'birth_date': '2000-10-10',
            'birth_country': 'TestCountry',
            'passport_id': 'PassporId123',
            'expiry_passport_date': '2025-10-10',
            'document_maker': 'testMaker',
            'photo': self.create_test_image()
        }
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 403)

    def test_authorized_with_permission_post_create_add(self):
        url = reverse('hostelguests:guest_create')
        data = {
            'first_name': 'Testname',
            'last_name': 'Test',
            'middle_name': 'TestMiddle',
            'birth_date': '2000-10-10',
            'birth_country': 'TestCountry',
            'passport_id': 'PassportId123',
            'expiry_passport_date': '2025-10-10',
            'document_maker': 'testMaker',
            'photo': self.create_test_image()
        }
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(url, data)
        guest = Guest.objects.order_by('pk').last()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        redirect_url = reverse('hostelguests:guest_list')
        self.assertEqual(response.url, redirect_url)
        self.assertEqual(guest.first_name, data['first_name'])
        self.assertEqual(guest.last_name, data['last_name'])
        self.assertEqual(guest.middle_name, data['middle_name'])
        self.assertTrue(guest.photo)








