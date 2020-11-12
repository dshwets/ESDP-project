from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.test import TestCase
from django.urls import reverse

from accounts.factories import UserFactory
from hostelguests.factories import GuestFactory


class GuestListTestCase(TestCase):
    def check_redirect(self, response, redirect_url):
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        self.assertEqual(response.url, redirect_url)

    def test_guest_list_logouted_request(self):
        response = self.client.get(reverse('hostelguests:guest_list'))
        redirect_url = reverse('accounts:login') + '?next=' + reverse('hostelguests:guest_list')
        self.check_redirect(response, redirect_url)

    def test_guest_list_logined_request(self):
        user = UserFactory(username='some_admin')
        self.client.login(username='some_admin', password='pass')
        GuestFactory(first_name='AB', last_name = 'C')
        response = self.client.get(reverse('hostelguests:guest_list'))
        response_empty_search = self.client.get(reverse('hostelguests:guest_list') + '?search=')
        response_succes_search = self.client.get(reverse('hostelguests:guest_list') + '?search=a')
        response_failed_search = self.client.get(reverse('hostelguests:guest_list') + '?search=D')

        self.assertEqual(response.context_data['guests'][0], response_empty_search.context_data['guests'][0])
        self.assertEqual(response.context_data['guests'].count(), response_empty_search.context_data['guests'].count())

        self.assertEqual(response.context_data['guests'][0], response_succes_search.context_data['guests'][0])
        self.assertEqual(response.context_data['guests'].count(), response_succes_search.context_data['guests'].count())

        self.assertNotEqual(response.context_data['guests'], response_failed_search.context_data['guests'])
        self.assertNotEqual(response.context_data['guests'].count(), response_failed_search.context_data['guests'].count())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), TemplateResponse)
        self.assertTemplateUsed(response, 'guests.html')
        self.client.logout()

