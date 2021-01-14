import datetime

from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.test import TestCase
from django.urls import reverse

from accounts.factories import UserFactory
from hostelguests.factories import GuestFactory
from hostelguests.models import Guest


class GuestBirthdayListTestCase(TestCase):
    def setUp(self):
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        self.guest = GuestFactory(birth_date=datetime.date.today())
        self.guest = GuestFactory(birth_date=yesterday)
        self.user = UserFactory(username='some_admin')
        self.url = reverse('hostelguests:guest_birthday_list')

    def tearDown(self) -> None:
        self.client.logout()

    def check_redirect(self, response, redirect_url):
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        self.assertEqual(response.url, redirect_url)

    def test_guest_birthday_list_logouted_request(self):
        response = self.client.get(self.url)
        redirect_url = reverse('accounts:login') + '?next=' + self.url
        self.check_redirect(response, redirect_url)

    def test_guest_birthday_list_logined_request(self):
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(self.url)
        now = datetime.datetime.now()
        self.assertQuerysetEqual(Guest.objects.filter(birth_date__day=now.day, birth_date__month=now.month),
                                 map(repr, response.context_data['guests']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), TemplateResponse)
        self.assertTemplateUsed(response, 'guest_birthday_list.html')
        self.client.logout()