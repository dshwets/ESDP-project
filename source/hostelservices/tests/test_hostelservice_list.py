from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.test import TestCase
from django.urls import reverse

from hostelguests.models import Guest
from accounts.factories import UserFactory
from hostelguests.factories import GuestFactory
from hostelservices.factories import HostelServiceFactory
from hostelservices.models import HostelService


class GuestListTestCase(TestCase):
    def check_redirect(self, response, redirect_url):
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        self.assertEqual(response.url, redirect_url)

    def test_guest_list_logouted_request(self):
        response = self.client.get(reverse('hostelservices:hostelservices_list'))
        redirect_url = reverse('accounts:login') + '?next=' + reverse('hostelservices:hostelservices_list')
        self.check_redirect(response, redirect_url)

    def test_guest_list_logined_request(self):
        user = UserFactory(username='some_admin')
        self.client.login(username='some_admin', password='pass')
        HostelServiceFactory(service_name='Some_service1')
        response = self.client.get(reverse('hostelservices:hostelservices_list'))
        self.assertQuerysetEqual(HostelService.objects.all(), map(repr, response.context_data['hostel_services']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), TemplateResponse)
        self.assertTemplateUsed(response, 'hostelguestservices_list.html')
        self.client.logout()

