from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponseRedirect

from aboutguests.factories import NoteFactory
from aboutguests.models import Note
from accounts.factories import UserFactory
from hostelguests.factories import GuestFactory


class NoteCreateTestCase(TestCase):
    def setUp(self) -> None:
        self.note = NoteFactory(guest=GuestFactory())
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_add_note')

    def tearDown(self) -> None:
        self.client.logout()

    def test_unauthorized_get_create_note(self):
        response = self.client.get(reverse('hostelguests:note:note_create', kwargs={'pk':self.note.guest.pk}))
        redirect_url = reverse('accounts:login') + '?next=' + reverse('hostelguests:note:note_create', kwargs={'pk':self.note.guest.pk})
        self.assertRedirects(response, redirect_url, status_code=302)

    def test_unauthorized_post_create_note(self):
        response = self.client.post(reverse('hostelguests:note:note_create', kwargs={'pk':self.note.guest.pk}))
        redirect_url = reverse('accounts:login') + '?next=' + reverse('hostelguests:note:note_create', kwargs={'pk':self.note.guest.pk})
        self.check_redirect(response, redirect_url)

    def check_redirect(self, response, redirect_url):
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        self.assertEqual(response.url, redirect_url)

    def test_authorized_without_permission_get_create_note(self):
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(reverse('hostelguests:note:note_create', kwargs={'pk':self.note.guest.pk}))
        self.assertEqual(response.status_code, 403)

    def test_authorized_without_permission_post_create_note(self):
        url = reverse('hostelguests:note:note_create', kwargs={'pk':self.note.guest.pk})
        data = {
            'description': self.note.description,
            'guest': self.note.guest
        }
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 403)

    def test_authorized_with_permission_post_create_note(self):
        url = reverse('hostelguests:note:note_create', kwargs={'pk':self.note.guest.pk})
        sucess_data = {
            'description': self.note.description,
            'guest': self.note.guest
        }
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        sucess_response = self.client.post(url, sucess_data)
        note = Note.objects.last()
        self.assertEqual(sucess_response.status_code, 302)
        self.assertEqual(type(sucess_response), HttpResponseRedirect)
        redirect_url = reverse('hostelguests:detail_view', kwargs={'pk':self.note.guest.pk})
        self.assertEqual(sucess_response.url, redirect_url)
        self.assertEqual(note.description, sucess_data['description'])
        self.assertEqual(note.guest, sucess_data['guest'])
