from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from aboutguests.factories import NoteFactory
from accounts.factories import UserFactory
from hostelguests.factories import GuestFactory


class NoteDeleteTestCase(TestCase):
    def setUp(self) -> None:
        self.guest = GuestFactory()
        self.note = NoteFactory(guest=self.guest)
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_delete_note')

    def tearDown(self) -> None:
        self.note.delete()
        self.user.delete()
        self.guest.delete()

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)

    def test_note_delete_unauthorized_get_request(self):
        self.assert_response_status(reverse('hostelguests:note_delete', args=(self.note.id,)), 'get', 302)

    def test_note_delete_unauthorized_post_request(self):
        self.assert_response_status(reverse('hostelguests:note_delete', args=(self.note.id,)), 'post', 302)

    def test_note_delete_authorized_request_no_perm(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(reverse('hostelguests:note_delete', args=(self.note.id,)), 'get', 403)

    def test_note_delete_authorized_get_request_has_perm(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        self.assertTemplateUsed('guest_delete.html')
        self.assert_response_status(reverse('hostelguests:note_delete', args=(self.note.id,)), 'get', 200)

    def test_note_delete_authorized_post_request_has_perm(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(reverse('hostelguests:note_delete', args=(self.note.id,)), 'post', 302)

    def test_note_delete_authorized_post_request_has_perm_guest_not_found(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        guest_wrong_id = self.note.id+10
        self.assert_response_status(reverse('hostelguests:note_delete', args=(guest_wrong_id,)), 'get', 404)
