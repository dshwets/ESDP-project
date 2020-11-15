from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponseRedirect

from aboutguests.factories import NoteFactory
from aboutguests.models import Note
from accounts.factories import UserFactory
from hostelguests.factories import GuestFactory


class GuestUpdateTestCase(TestCase):
    def setUp(self) -> None:
        self.note = NoteFactory(guest=GuestFactory())
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_change_note')

    def tearDown(self) -> None:
        self.client.logout()

    def test_unauthorized_get_update_note(self):
        response = self.client.get(reverse('aboutguests:note_update', kwargs={'pk':self.note.pk}))
        redirect_url = reverse('accounts:login') + '?next=' + reverse('aboutguests:note_update', kwargs={'pk':self.note.pk})
        self.assertRedirects(response, redirect_url, status_code=302)

    def test_unauthorized_post_update_note(self):
        response = self.client.post(reverse('aboutguests:note_update', kwargs={'pk':self.note.pk}))
        redirect_url = reverse('accounts:login') + '?next=' + reverse('aboutguests:note_update', kwargs={'pk':self.note.pk})
        self.check_redirect(response, redirect_url)

    def check_redirect(self, response, redirect_url):
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        self.assertEqual(response.url, redirect_url)

    def test_authorized_without_permission_get_update_note(self):
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(reverse('aboutguests:note_update', kwargs={'pk':self.note.pk}))
        self.assertEqual(response.status_code, 403)

    def test_authorized_without_permission_post_update_note(self):
        url = reverse('aboutguests:note_update', kwargs={'pk':self.note.pk})
        data = {
            'description': self.note.description,
            'guest': self.note.guest
        }
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 403)

    def test_authorized_with_permission_post_update_note(self):
        url = reverse('aboutguests:note_update', kwargs={'pk':self.note.pk})
        data = {
            'description': 'TestDescription',
            'guest': self.note.guest.pk
        }
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        redirect_url = reverse('hostelguests:detail_view',kwargs={'pk':self.note.guest.pk})
        self.assertEqual(response.url, redirect_url)
        note = Note.objects.get(pk=self.note.pk)
        self.assertEqual(note.guest.pk, data['guest'])
        self.assertEqual(note.description, data['description'])