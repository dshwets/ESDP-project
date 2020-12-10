from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from serviceexecutors.factories import ServiceExecutorFactory
from accounts.factories import UserFactory
from serviceexecutors.models import ServiceExecutor


class NoteDeleteTestCase(TestCase):
    def setUp(self) -> None:
        self.serviceexecutor = ServiceExecutorFactory()
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_delete_serviceexecutor')

    def tearDown(self) -> None:
        self.client.logout()

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)

    def test_serviceexecutor_delete_unauthorized_get_request(self):
        self.assert_response_status(reverse('serviceexecutors:serviceexecutor_delete', args=(self.serviceexecutor.pk,)), 'get', 302)

    def test_serviceexecutor_delete_unauthorized_post_request(self):
        self.assert_response_status(reverse('serviceexecutors:serviceexecutor_delete', args=(self.serviceexecutor.pk,)), 'post', 302)

    def test_serviceexecutor_delete_authorized_request_no_perm(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(reverse('serviceexecutors:serviceexecutor_delete', args=(self.serviceexecutor.pk,)), 'get', 403)

    def test_serviceexecutor_delete_authorized_post_request_has_perm_serviceexecutor_not_found(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        fake_id = self.serviceexecutor.id+25
        self.assert_response_status(reverse('serviceexecutors:serviceexecutor_delete', args=(fake_id,)), 'get', 404)

    def test_authorized_request_has_perm_delete_serviceexecutor(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        url = reverse('serviceexecutors:serviceexecutor_delete', args=(self.serviceexecutor.pk,))
        redirect_url = reverse('serviceexecutors:serviceexecutors_list')
        response = self.client.post(url)
        self.assertRedirects(response=response, expected_url=redirect_url, status_code=302,
                             target_status_code=200, msg_prefix='', fetch_redirect_response=True)
        self.assertFalse(ServiceExecutor.objects.filter(pk=self.serviceexecutor.pk).exists())
