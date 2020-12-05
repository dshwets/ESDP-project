from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponseRedirect
from accounts.factories import UserFactory
from documents.factories import DocumentFactory
from django.core.files.base import ContentFile


from serviceexecutors.factories import ServiceExecutorFactory


class GuestCreateTestCase(TestCase):
    def setUp(self) -> None:
        self.serviceexecutor = ServiceExecutorFactory()
        self.document = DocumentFactory()
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_add_document')
        self.url = reverse('documents:doc_add', kwargs={'pk': self.serviceexecutor.pk})


    def tearDown(self) -> None:
        self.client.logout()


    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            print(response)
            self.assertEqual(response.status_code, code)

    def common_data(self):
        fake_file = ContentFile(b"Some file content")
        fake_file.name = 'myfile.doc'
        data = {
            'title': 'TestTitle',
            'service_executor': self.serviceexecutor.pk,
            'file':fake_file
        }
        return data


    def test_unauthorized_get_create_document(self):
        self.assert_response_status(self.url, 'get', 302)

    def test_unauthorized_post_create_document(self):
        self.assert_response_status(self.url, 'post', 302)

    def test_authorized_without_permission_get_create_document(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(self.url, 'post', 403)

    def test_authorized_without_permission_post_create_document(self):
        data = self.common_data()
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 403)

    def test_authorized_get_request_has_perm_create_document(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        self.assertTemplateUsed('document_update.html')
        self.assert_response_status(self.url, 'get', 200)

    def testauthorized_post_request_has_perm_create_document(self):
        data = self.common_data()
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.serviceexecutor.pk, data['service_executor'])
        self.assertEqual(type(response), HttpResponseRedirect)
        redirect_url = reverse('serviceexecutors:serviceexecutor_view', kwargs={'pk': self.serviceexecutor.pk})
        self.assertEqual(response.url, redirect_url)