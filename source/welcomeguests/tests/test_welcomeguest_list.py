from django.test import TestCase
from django.urls import reverse
from accounts.factories import UserFactory
from hostelguests.factories import GuestFactory
from welcomeguests.factories import WelcomeGuestFactory


class WelcomeGuestListTestCase(TestCase):
    def setUp(self) -> None:
        self.welcomguest = WelcomeGuestFactory(guest=GuestFactory())
        self.user = UserFactory(username='some_admin')

    def tearDown(self) -> None:
        self.client.logout()

    def test_unauthorized_get_welcome_guest_list(self):
        response = self.client.get(reverse('welcomeguests:welcome_guest_list'))
        redirect_url = reverse('accounts:login') + '?next=' + reverse('welcomeguests:welcome_guest_list')
        self.assertRedirects(response, redirect_url, status_code=302)

    def test_authorized_get_welcome_guest_list(self):
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(reverse('welcomeguests:welcome_guest_list'))
        self.assertEqual(response.status_code, 200)



