from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse

class GuestListTestCase(TestCase):
    def check_redirect(self, response, redirect_url):
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        self.assertEqual(response.url, redirect_url)

    def test_welcome_guest_list_logouted_request(self):
        response = self.client.get(reverse('welcomeguests:welcome_guest_list'))
        redirect_url = reverse('accounts:login') + '?next=' + reverse('welcomeguests:welcome_guest_list')
        self.check_redirect(response, redirect_url)

