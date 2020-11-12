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

    def test_anonymous_request(self):
        response = self.client.get(reverse('hostelguests:guest_delete', args=(self.guest.id,)))
        redirect_url = reverse('accounts:login') + '?next=' + reverse('hostelguests:guest_delete', args=(self.guest.id,))
        self.assertRedirects(response, redirect_url, status_code=302)

    def test_unauthorized_request(self):
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(reverse('hostelguests:guest_delete', args=(self.guest.id,)), follow=True)
        self.assertEqual(response.status_code, 403)

    def test_authorized_get_request(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(reverse('hostelguests:guest_delete', args=(self.guest.id,)), follow=True)
        self.assertContains(response, 'Вы уверены, что хотите удалить гостя')

    def test_authorized_post_request(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        post_response = self.client.post(reverse('hostelguests:guest_delete', args=(self.guest.id,)), follow=True)
        self.assertRedirects(post_response, reverse('hostelguests:guest_list'), status_code=302)
