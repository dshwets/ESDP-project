from django.test import TestCase
from django.contrib.auth.models import Permission
from django.http import HttpResponseRedirect
from django.urls import reverse
from accounts.factories import UserFactory
from hostelguests.factories import GuestFactory
from hostelservices.factories import HostelServiceFactory, PurchasePriceFactory, SellingPriceFactory
from journalservices.factories import JournalServiceFactory
from serviceexecutors.factories import ServiceExecutorFactory


class JournalServiceCreateTestCase(TestCase):
    def setUp(self) -> None:
        self.permission = Permission.objects.get(codename='can_add_journalservice')
        self.journal = JournalServiceFactory(
            guest=GuestFactory(),
            hostel_service=HostelServiceFactory(),
            service_executor=ServiceExecutorFactory(),
            purchase_price=PurchasePriceFactory(),
            selling_price=SellingPriceFactory()
        )
        self.guest = GuestFactory(),
        self.user = UserFactory(username='some_admin')

    def tearDown(self) -> None:
        self.client.logout()

    def check_redirect(self, response, redirect_url):
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        self.assertEqual(response.url, redirect_url)

    def test_unauthorized_get_create_journal_service(self):
        response = self.client.get(reverse('journalservices:journal_create', kwargs={'guest_pk':self.journal.guest.pk}))
        redirect_url = reverse('accounts:login') + '?next=' + reverse('journalservices:journal_create', kwargs={'guest_pk':self.journal.guest.pk})
        self.assertRedirects(response, redirect_url, status_code=302)

    def test_unauthorized_post_create_journal_service(self):
        response = self.client.post(reverse('journalservices:journal_create', kwargs={'guest_pk':self.journal.guest.pk}))
        redirect_url = reverse('accounts:login') + '?next=' + reverse('journalservices:journal_create', kwargs={'guest_pk':self.journal.guest.pk})
        self.check_redirect(response, redirect_url)

    def test_authorized_without_permission_get_create_journal_service(self):
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(reverse('journalservices:journal_create', kwargs={'guest_pk':self.journal.guest.pk}))
        self.assertEqual(response.status_code, 403)

    def test_authorized_without_permission_post_create_journal_service(self):
        url = reverse('journalservices:journal_create', kwargs={'guest_pk':self.journal.guest.pk})
        data = {
            'guest': self.journal.guest,
            'hostel_service': self.journal.hostel_service,
            'service_executor':self.journal.service_executor,
            'purchase_price':self.journal.purchase_price,
            'selling_price': self.journal.selling_price,
        }
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 403)

    def test_authorized_with_permission_post_create_journal_service(self):
        url = reverse('journalservices:journal_create', kwargs={'guest_pk':self.journal.guest.pk})
        data = {
            'hostel_service': self.journal.hostel_service.pk,
            'service_executor': self.journal.service_executor.pk,
            'purchase_price': self.journal.purchase_price.pk,
            'selling_price': self.journal.selling_price.pk,
        }
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        redirect_url = reverse('journalservices:journal_list')
        self.assertEqual(response.url, redirect_url)


