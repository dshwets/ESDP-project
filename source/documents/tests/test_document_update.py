from django.contrib.auth.models import Permission
from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse
from accounts.factories import UserFactory
from documents.factories import DocumentFactory
from documents.models import Document
from serviceexecutors.factories import ServiceExecutorFactory


class DocumentUpdateTestCase(TestCase):
    def setUp(self) -> None:
        self.document = DocumentFactory()
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_change_document')
        self.url = reverse('documents:document_update', kwargs={'pk': self.document.pk})
        self.serviceexecutor = self.document.service_executor

    def tearDown(self) -> None:
        self.client.logout()

    def common_data(self):
        fake_file = ContentFile(b"Some file content")
        fake_file.name = 'myfile.xml'
        data = {
            'title': 'TestTitle',
            'service_executor': self.serviceexecutor.pk
        }
        return data

    def test_unauthorized_get_update_document(self):
        self.assert_response_status(self.url, 'get', 302)

    def test_unauthorized_post_update_document(self):
        self.assert_response_status(self.url, 'post', 302)

    def test_authorized_without_permission_get_update_document(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(self.url, 'post', 403)

    def test_authorized_without_permission_post_update_document(self):
        data = self.common_data()
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 403)

    def test_authorized_get_request_has_perm_update_document(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        self.assertTemplateUsed('document_update.html')
        self.assert_response_status(self.url, 'get', 200)

    def test_authorized_with_permission_post_update_document(self):
        data = self.common_data()
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        document = Document.objects.get(pk=self.document.pk)
        self.assertEqual(document.title, data['title'])
        self.assertEqual(document.service_executor.pk, data['service_executor'])
        self.assertEqual(type(response), HttpResponseRedirect)
        redirect_url = reverse('serviceexecutors:serviceexecutor_view', kwargs={'pk': self.serviceexecutor.pk})
        self.assertEqual(response.url, redirect_url)

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)