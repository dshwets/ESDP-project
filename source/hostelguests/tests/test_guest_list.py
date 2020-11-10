from django.contrib.auth import get_user_model
from django.db.models import Model
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.test import TestCase
from django.urls import reverse


class NotAuthenticatedGuestListTestCase(TestCase):
    def check_redirect(self, response, redirect_url):
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        self.assertEqual(response.url, redirect_url)

    def test_logouted_request(self):
        response = self.client.get(reverse('hostelguests:guest_list'))
        redirect_url = reverse('accounts:login') + '?next=' + reverse('hostelguests:guest_list')
        self.check_redirect(response, redirect_url)


class AuthenticatdGuestListTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        User: Model = get_user_model()
        user, created = User.objects.get_or_create(username='admin')
        if created:
            user.set_password('admin')
            user.save()

    def setUp(self):
        self.client.login(username='admin', password='admin')

    def tearDown(self) -> None:
        self.client.logout()

    def test_logined_request(self):
        response = self.client.get(reverse('hostelguests:guest_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), TemplateResponse)

