from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from accounts.factories import UserFactory
from serviceexecutors.factories import ServiceExecutorFactory


class ServiceExecutorCreateTestCase(TestCase):
    def setUp(self) -> None:
        self.serviceexecutor = ServiceExecutorFactory()
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_add_serviceexecutor')

    def tearDown(self) -> None:
        self.client.logout()

    def test_unauthorized_get_create_serviceexecutor(self):
        self.assert_response_status(reverse('serviceexecutors:serviceexecutor_create'), 'get', 302)

    def test_unauthorized_post_create_serviceexecutor(self):
        self.assert_response_status(reverse('serviceexecutors:serviceexecutor_create'), 'post', 302)

    def test_authorized_without_permission_get_create_serviceexecutor(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(reverse('serviceexecutors:serviceexecutor_create'), 'post', 403)

    def test_authorized_without_permission_post_create_serviceexecutor(self):
        url = reverse('serviceexecutors:serviceexecutor_create')
        data = {
            'name': self.serviceexecutor.name,
            'last_name': self.serviceexecutor.last_name,
            'middle_name': self.serviceexecutor.middle_name,
        }
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 403)

    def test_authorized_get_request_has_perm_create_serviceexecutor(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        self.assertTemplateUsed('serviceexecutor_create.html')
        self.assert_response_status(reverse('serviceexecutors:serviceexecutor_create'), 'get', 200)

    def test_authorized_post_request_has_perm_create_serviceexecutor(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        data = data = {
            'name': self.serviceexecutor.name,
            'last_name': self.serviceexecutor.last_name,
            'middle_name': self.serviceexecutor.middle_name,
        }
        url = reverse('serviceexecutors:serviceexecutor_create')
        redirect_url = reverse('hostelguests:guest_list')
        response = self.client.post(url, data)
        self.assertRedirects(response=response, expected_url=redirect_url, status_code=302,
                             target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_authorized_with_permission_post_create_serviceexecutor_with_empty_name(self):
        url = reverse('serviceexecutors:serviceexecutor_create')
        data = data = {
            'name': '',
            'last_name': self.serviceexecutor.last_name,
            'middle_name': self.serviceexecutor.middle_name,
        }
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(url, data)
        field = 'name'
        self.assertFormError(response, 'form', field, 'Обязательное поле.')

    def test_authorized_with_permission_post_create_serviceexecutor_with_empty_last_name(self):
        url = reverse('serviceexecutors:serviceexecutor_create')
        data = data = {
            'name': self.serviceexecutor.name,
            'last_name': '',
            'middle_name': self.serviceexecutor.middle_name,
        }
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(url, data)
        field = 'last_name'
        self.assertFormError(response, 'form', field, 'Обязательное поле.')

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)
