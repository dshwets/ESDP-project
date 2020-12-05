from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from accounts.factories import UserFactory
from hostelservices.factories import HostelServiceFactory
from hostelservices.models import HostelService


class HostelServiceDeleteTestCase(TestCase):
    def setUp(self) -> None:
        self.hostelservice = HostelServiceFactory()
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_delete_hostelservice')

    def tearDown(self) -> None:
        self.client.logout()

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)

    def test_hostelservice_delete_unauthorized_get_request(self):
        self.assert_response_status(reverse('hostelservices:hostelservice_delete',
                                            args=(self.hostelservice.pk,)), 'get', 302)

    def test_hostelservice_delete_authorized_request_no_perm(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(reverse('hostelservices:hostelservice_delete',
                                            args=(self.hostelservice.pk,)), 'get', 403)

    def test_hostelservice_delete_authorized_request_has_perm(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        url = reverse('hostelservices:hostelservice_delete', args=(self.hostelservice.pk,))
        redirect_url = reverse('hostelservices:hostelservices_list')
        response = self.client.post(url)
        self.assertTemplateUsed('hostelservice_delete.html')
        self.assertRedirects(response=response, expected_url=redirect_url, status_code=302,
                             target_status_code=200, msg_prefix='', fetch_redirect_response=True)
        self.assertFalse(HostelService.objects.filter(pk=self.hostelservice.pk).exists())

    def test_hostelservice_delete_authorized_post_request_has_perm_hostelservice_not_found(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        fake_id = self.hostelservice.id+15
        self.assert_response_status(reverse('hostelservices:hostelservice_delete',
                                            args=(fake_id,)), 'get', 404)
