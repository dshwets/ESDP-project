from django.test import TestCase
from django.contrib.auth.models import Permission
from django.http import HttpResponseRedirect
from django.urls import reverse
from accounts.factories import UserFactory
from hostelguests.factories import GuestFactory
from hostelservices.factories import HostelServiceFactory, PurchasePriceFactory, SellingPriceFactory
from journalservices.factories import JournalServiceFactory
from serviceexecutors.factories import ServiceExecutorFactory


class JournalServicetListTestCase(TestCase):
    def setUp(self) -> None:
        self.permission = Permission.objects.get(codename='can_view_journalservice')
        self.journal = JournalServiceFactory(
            guest=GuestFactory(),
            hostel_service=HostelServiceFactory(),
            service_executor=ServiceExecutorFactory(),
            purchase_price=PurchasePriceFactory(),
            selling_price=SellingPriceFactory()
        )
        self.user = UserFactory(username='some_admin')

    def tearDown(self) -> None:
        self.client.logout()

    def check_redirect(self, response, redirect_url):
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        self.assertEqual(response.url, redirect_url)

    def test_unauthorized_get_journalservice_list(self):
        url = reverse('journalservices:journal_list')
        response = self.client.get(url)
        redirect_url = reverse('accounts:login') + '?next=' + url
        self.check_redirect(response, redirect_url)

    def test_authorized_without_permission_get_journalservice_list(self):
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(reverse('journalservices:journal_list'), follow=True)
        self.assertEqual(response.status_code, 403)

    def test_authorized_with_permission_get_hostelservices_detail(self):
        self.client.login(username='some_admin', password='pass')
        self.user.user_permissions.add(self.permission)
        response = self.client.get(reverse('journalservices:journal_list'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'journalservices_list.html')