from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from accounts.factories import UserFactory
from documents.factories import DocumentFactory
from serviceexecutors.factories import ServiceExecutorFactory


class GuestDeleteTestCase(TestCase):
    def setUp(self) -> None:
        self.document = DocumentFactory()
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_delete_document')
        self.url = reverse('documents:document_delete', kwargs={'pk': self.document.pk})
        self.serviceexecutor = ServiceExecutorFactory()

    def tearDown(self) -> None:
        self.client.logout()

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)

    def test_document_delete_unauthorized_get_request(self):
        self.assert_response_status(self.url, 'get', 302)

    def test_document_delete_unauthorized_post_request(self):
        self.assert_response_status(self.url, 'post', 302)

    def test_document_delete_authorized_request_no_perm(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(self.url, 'get', 403)

    def test_document_delete_authorized_post_request_has_perm(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(self.url, 'post', 302)

    def test_document_delete_authorized_post_request_has_perm_guest_not_found(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        document_wrong_id = self.document.id+10
        self.assert_response_status(reverse('documents:document_delete', args=(document_wrong_id,)), 'get', 404)