from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from accounts.factories import UserFactory
from hostelguests.factories import GuestFactory
from welcomeguests.factories import WelcomeGuestFactory


class WelcomeGuestDeleteTestCase(TestCase):
    def setUp(self) -> None:
        self.guest = GuestFactory()
        self.welcomeguest = WelcomeGuestFactory(guest=self.guest)
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_delete_welcomeguest')

    def tearDown(self) -> None:
        self.client.logout()

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)