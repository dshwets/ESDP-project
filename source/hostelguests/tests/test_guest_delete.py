from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from accounts.factories import UserFactory
from hostelguests.factories import GuestFactory


class GuestDeleteTestCase(TestCase):
    def setUp(self) -> None:
        self.guest = GuestFactory()
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_delete_guest')

    def tearDown(self) -> None:
        self.guest.delete()
        self.user.delete()

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)

    def test_guest_delete_unauthorized_get_request(self):
        self.assert_response_status(reverse('hostelguests:guest_delete', args=(self.guest.id,)), 'get', 302)

    def test_guest_delete_unauthorized_post_request(self):
        self.assert_response_status(reverse('hostelguests:guest_delete', args=(self.guest.id,)), 'post', 302)

    def test_guest_delete_authorized_request_no_perm(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(reverse('hostelguests:guest_delete', args=(self.guest.id,)), 'get', 403)

    def test_guest_delete_authorized_get_request_has_perm(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        self.assertTemplateUsed('guest_delete.html')
        self.assert_response_status(reverse('hostelguests:guest_delete', args=(self.guest.id,)), 'get', 200)

    def test_guest_delete_authorized_post_request_has_perm(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(reverse('hostelguests:guest_delete', args=(self.guest.id,)), 'post', 302)

    def test_guest_delete_authorized_post_request_has_perm_guest_not_found(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        guest_wrong_id = self.guest.id+10
        self.assert_response_status(reverse('hostelguests:guest_delete', args=(guest_wrong_id,)), 'get', 404)
