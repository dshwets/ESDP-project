from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from accounts.factories import UserFactory
from journalservices.factories import JournalServiceFactory
from journalservices.models import JournalService


class JournalserviceDeleteTestCase(TestCase):
    def setUp(self) -> None:
        self.journalservice = JournalServiceFactory()
        self.user = UserFactory(username='some_admin', password='pass')
        self.permission = Permission.objects.get(codename='can_delete_journalservice')

    def tearDown(self) -> None:
        self.client.logout()

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)

    def test_journalservice_delete_unauthorized_get_request(self):
        self.assert_response_status(reverse('journalservices:journal_delete',
                                            args=(self.journalservice.id,)), 'get', 302)

    def test_journalservice_delete_unauthorized_post_request(self):
        self.assert_response_status(reverse('journalservices:journal_delete',
                                            args=(self.journalservice.id,)), 'post', 302)

    def test_journalservice_delete_authorized_request_no_perm(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(reverse('journalservices:journal_delete',
                                            args=(self.journalservice.id,)), 'get', 403)

    def test_journalservice_delete_authorized_get_request_has_perm(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        self.assertTemplateUsed('guest_delete.html')
        self.assert_response_status(reverse('journalservices:journal_delete',
                                            args=(self.journalservice.id,)), 'get', 200)

    def test_journalservice_delete_authorized_post_request_has_perm(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(reverse('journalservices:journal_delete',
                                            args=(self.journalservice.id,)), 'post', 302)
        self.assertFalse(JournalService.objects.all().exists())

    def test_journalservice_delete_authorized_post_request_has_perm_guest_not_found(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        wrong_id = self.journalservice.id+10
        self.assert_response_status(reverse('journalservices:journal_delete',
                                            args=(wrong_id,)), 'get', 404)
