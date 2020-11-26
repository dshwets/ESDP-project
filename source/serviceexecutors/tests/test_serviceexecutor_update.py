from django.contrib.auth.models import Permission
from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse
from accounts.factories import UserFactory
from serviceexecutors.factories import ServiceExecutorFactory
from serviceexecutors.models import ServiceExecutor


class ServiceExecutorUpdateTestCase(TestCase):
    def setUp(self) -> None:
        self.serviceexecutor = ServiceExecutorFactory()
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_change_serviceexecutor')
        self.url = reverse('serviceexecutors:serviceexecutor_update', kwargs={'pk': self.serviceexecutor.pk})

    def tearDown(self) -> None:
        self.client.logout()

    def common_data(self):
        data = {
            'name': 'TestName',
            'last_name': 'TestLastName',
            'middle_name': 'TestMiddleName',
        }
        return data

    def test_unauthorized_get_update_serviceexecutor(self):
        self.assert_response_status(self.url, 'get', 302)

    def test_unauthorized_post_update_serviceexecutor(self):
        self.assert_response_status(self.url, 'post', 302)

    def test_authorized_without_permission_get_update_serviceexecutor(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(self.url, 'post', 403)

    def test_authorized_without_permission_post_update_serviceexecutor(self):
        data = self.common_data()
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 403)

    def test_authorized_get_request_has_perm_update_serviceexecutor(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        self.assertTemplateUsed('serviceexecutor_update.html')
        self.assert_response_status(self.url, 'get', 200)

    def test_authorized_with_permission_post_update_serviceexecutor(self):
        data = self.common_data()
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        executor = ServiceExecutor.objects.get(pk=self.serviceexecutor.pk)
        self.assertEqual(executor.name, data['name'])
        self.assertEqual(executor.last_name, data['last_name'])
        self.assertEqual(executor.middle_name, data['middle_name'])
        self.assertEqual(type(response), HttpResponseRedirect)
        redirect_url = reverse('hostelguests:guest_list')
        self.assertEqual(response.url, redirect_url)

    def test_authorized_with_permission_post_update_serviceexecutor_with_empty_name(self):
        data = data = {
            'name': '',
            'last_name': self.serviceexecutor.last_name,
            'middle_name': self.serviceexecutor.middle_name,
        }
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        field = 'name'
        self.assertFormError(response, 'form', field, 'Обязательное поле.')

    def test_authorized_with_permission_post_update_serviceexecutor_with_empty_last_name(self):
        data = data = {
            'name': self.serviceexecutor.name,
            'last_name': '',
            'middle_name': self.serviceexecutor.middle_name,
        }
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        field = 'last_name'
        self.assertFormError(response, 'form', field, 'Обязательное поле.')

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)