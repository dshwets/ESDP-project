from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from accounts.factories import UserFactory
from hostelservices.factories import HostelServiceFactory
from serviceexecutors.factories import ServiceExecutorFactory
from serviceexecutors.models import ServiceExecutor


class ServiceExecutorCreateTestCase(TestCase):
    def setUp(self) -> None:
        self.serviceexecutor = ServiceExecutorFactory()
        self.hostel_service = HostelServiceFactory()
        self.user = UserFactory(username='some_admin')
        self.permission_add = Permission.objects.get(codename='can_add_serviceexecutor')
        self.permission_view = Permission.objects.get(codename='can_view_serviceexecutor')

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
            'name': 'test_name',
            'last_name': 'test_surname',
            'middle_name': 'test_middlename',
            'hostel_service': self.hostel_service.pk,
        }
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 403)

    def test_authorized_get_request_has_perm_create_serviceexecutor(self):
        self.user.user_permissions.add(self.permission_add)
        self.client.login(username='some_admin', password='pass')
        self.assertTemplateUsed('serviceexecutor_create.html')
        self.assert_response_status(reverse('serviceexecutors:serviceexecutor_create'), 'get', 200)

    def test_authorized_post_request_has_perm_create_serviceexecutor(self):
        self.user.user_permissions.add(self.permission_add)
        self.user.user_permissions.add(self.permission_view)
        self.client.login(username='some_admin', password='pass')
        data = {
            'name': 'test_name',
            'last_name': 'test_surname',
            'middle_name': 'test_middlename',
            'hostel_service': self.hostel_service.pk,
        }
        url = reverse('serviceexecutors:serviceexecutor_create')
        response = self.client.post(url, data)
        redirect_url = reverse('serviceexecutors:serviceexecutor_view',
                               args=(ServiceExecutor.objects.get(name='test_name').pk,))
        self.assertRedirects(response=response, expected_url=redirect_url, status_code=302,
                             target_status_code=200, msg_prefix='', fetch_redirect_response=True)
        self.assertTrue(ServiceExecutor.objects.filter(name='test_name').exists())

    def test_authorized_with_permission_post_create_serviceexecutor_with_empty_name(self):
        url = reverse('serviceexecutors:serviceexecutor_create')
        data = {
            'name': '',
            'last_name': 'test_surname',
            'middle_name': 'test_middlename',
            'hostel_service': self.hostel_service.pk,
        }
        self.user.user_permissions.add(self.permission_add)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(url, data)
        field = 'name'
        self.assertFormError(response, 'form', field, 'Обязательное поле.')

    def test_authorized_with_permission_post_create_serviceexecutor_with_empty_last_name(self):
        url = reverse('serviceexecutors:serviceexecutor_create')
        data = {
            'name': 'test_name',
            'last_name': '',
            'middle_name': 'test_middlename',
            'hostel_service': self.hostel_service.pk,
        }
        self.user.user_permissions.add(self.permission_add)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(url, data)
        field = 'last_name'
        self.assertFormError(response, 'form', field, 'Обязательное поле.')

    def test_authorized_with_permission_post_create_serviceexecutor_with_empty_hostel_service(self):
        url = reverse('serviceexecutors:serviceexecutor_create')
        data = {
            'name': 'test_name',
            'last_name': 'test_surname',
            'middle_name': 'test_middlename',
        }
        self.user.user_permissions.add(self.permission_add)
        self.client.login(username='some_admin', password='pass')
        self.client.post(url, data)
        self.assertTrue(ServiceExecutor.objects.filter(name='test_name').exists())

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)
