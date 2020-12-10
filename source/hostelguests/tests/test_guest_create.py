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

LONG_TEXT = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in'

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
        return ImageFile(file)

    def common_data(self):
        data = {
            'first_name': 'Testname',
            'last_name': 'Test',
            'middle_name': 'TestMiddle',
            'birth_date': '20.01.1980',
            'birth_country': 'KG',
            'passport_id': 'PassportId123',
            'expiry_passport_date': '10.05.2020',
            'document_maker': 'testMaker',
            'photo': self.create_test_image()
        }
        return data

    def test_authorized_without_permission_post_create_guest(self):
        url = reverse('hostelguests:guest_create')
        data = self.common_data()
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 403)

    def test_authorized_with_permission_post_create_guest(self):
        url = reverse('hostelguests:guest_create')
        data = self.common_data()
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(url, data)
        guest = Guest.objects.order_by('pk').last()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        redirect_url = reverse('hostelguests:detail_view', kwargs={'pk': guest.pk})
        self.assertEqual(response.url, redirect_url)
        self.assertEqual(guest.first_name, data['first_name'])
        self.assertEqual(guest.last_name, data['last_name'])
        self.assertEqual(guest.middle_name, data['middle_name'])
        self.assertEqual(guest.birth_country, data['birth_country'])
        self.assertEqual(guest.passport_id, data['passport_id'])
        self.assertEqual(guest.document_maker, data['document_maker'])
        self.assertTrue(guest.photo)

    def test_authorized_with_permission_post_create_guest_with_empty_first_name(self):
        url = reverse('hostelguests:guest_create')
        data = self.common_data()
        data['first_name'] = ''
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(url, data)
        field = 'first_name'
        self.assertFormError(response, 'form', field, 'Обязательное поле.')

    def test_authorized_with_permission_post_create_guest_with_empty_last_name(self):
        url = reverse('hostelguests:guest_create')
        data = self.common_data()
        data['last_name'] = ''
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(url, data)
        field = 'last_name'
        self.assertFormError(response, 'form', field, 'Обязательное поле.')

    def test_authorized_with_permission_post_create_guest_with_empty_birth_date(self):
        url = reverse('hostelguests:guest_create')
        data = self.common_data()
        data['birth_date'] = ''
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(url, data)
        field = 'birth_date'
        self.assertFormError(response, 'form', field, 'Обязательное поле.')

    def test_authorized_with_permission_post_create_guest_with_empty_country(self):
        url = reverse('hostelguests:guest_create')
        data = self.common_data()
        data['birth_country'] = ''
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(url, data)
        field = 'birth_country'
        self.assertFormError(response, 'form', field, 'Обязательное поле.')

    def test_authorized_with_permission_post_create_guest_with_empty_passport_id(self):
        url = reverse('hostelguests:guest_create')
        data = self.common_data()
        data['passport_id'] = ''
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(url, data)
        field = 'passport_id'
        self.assertFormError(response, 'form', field, 'Обязательное поле.')

    def test_authorized_with_permission_post_create_guest_with_invalid_birth_date(self):
        url = reverse('hostelguests:guest_create')
        data = self.common_data()
        data['birth_date'] = '2000-12-88'
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(url, data)
        field = 'birth_date'
        self.assertFormError(response, 'form', field, 'Введите правильную дату.')

    def test_authorized_with_permission_post_create_guest_with_invalid_expiry_passport_date(self):
        url = reverse('hostelguests:guest_create')
        data = self.common_data()
        data['expiry_passport_date'] = '2000-12-88'
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(url, data)
        field = 'expiry_passport_date'
        self.assertFormError(response, 'form', field, 'Введите правильную дату.')

    def test_authorized_with_permission_post_create_guest_with_long_first_name(self):
        url = reverse('hostelguests:guest_create')
        data = self.common_data()
        data['first_name'] = LONG_TEXT
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(url, data)
        field = 'first_name'
        self.assertFormError(response, 'form', field, 'Убедитесь, что это значение содержит не более 255 символов (сейчас 256).')

    def test_authorized_with_permission_post_create_guest_with_long_last_name(self):
        url = reverse('hostelguests:guest_create')
        data = self.common_data()
        data['last_name'] = LONG_TEXT
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(url, data)
        field = 'last_name'
        self.assertFormError(
            response, 'form', field, 'Убедитесь, что это значение содержит не более 255 символов (сейчас 256).'
        )

    def test_authorized_with_permission_post_create_guest_with_long_document_maker(self):
        url = reverse('hostelguests:guest_create')
        data = self.common_data()
        data['document_maker'] = LONG_TEXT
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(url, data)
        field = 'document_maker'
        self.assertFormError(
            response, 'form', field,'Убедитесь, что это значение содержит не более 255 символов (сейчас 256).'
        )